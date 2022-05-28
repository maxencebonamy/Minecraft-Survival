import random
from statistics import mean

from animation.flash import FlashAnimation
from animation.gradient import GradientAnimation
from animation.jump import JumpAnimation
from animation.linear import LinearAnimation
from animation.opacity import OpacityAnimation
from animation.resize import ResizeAnimation
from data.enum.colors import Color
from data.enum.effects import Effect
from data.enum.mobs import Mob
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from output.sound import Sound
from save import Save
from screen._screen import Screen
from util.anchor import Anchor
from widget.collection.cover import Cover
from widget.image import Image
from widget.rectangle import Rectangle
from widget.sprite import Sprite
from widget.text import Text


class OpenChestScreen(Screen):

    def __init__(self, window):
        """
        phase:
        objects:
        objActual:
        """

        super().__init__(window)

        Rules.BG_COLOR = Color.BG_DARK

        self.phase = 'idle'
        self.objects = self.draw()
        self.objActual = 0
        self.canClick = True

        # widgets
        self.widgets = {
            # coffre
            'chest': Sprite(self.window, self.cut.getPos(16, 5), self.cut.getSize(16, 16), 'chest'),
            # fondu blanc (invisible au début)
            'white': Rectangle(self.window, (0, 0), Rules.SCREEN_SIZE, (0, 0, 0)).setOpacity(0)
        }

        # animations
        self.widgets['chest'].animations.append(
            JumpAnimation(self.widgets['chest'], 0.5, 10)
        )

    def loop(self):
        super().loop()

        if self.phase == 'idle':
            self.loopIdle()
        elif self.phase == 'animation':
            self.loopAnimation()
        elif self.phase == 'object':
            self.loopObject()

    def loopIdle(self):
        if Input.clic:
            Sound.playSound(Sound.CHEST)
            self.phase = 'animation'
            self.widgets['chest'].spriteContinue = False
            self.widgets['chest'].setSprited(0.5).animations.clear()
            self.widgets['white'].animations.append(OpacityAnimation(self.widgets['white'], 30, 255))

    def loopAnimation(self):
        if self.widgets.get('chest') and not self.widgets['chest'].isSprited:
            del self.widgets['chest']
        if not self.widgets['white'].animations and not self.widgets.get('chest'):
            del self.widgets['white']
            self.phase = 'object'

    def loopObject(self):
        if not self.objects:
            self.nextScreen = 'menu'

        else:
            obj = self.objects[self.objActual]
            level = Save.read(Save.getPath(obj.kind, obj.name))

            if not self.widgets.get('object'):
                Rules.BG_COLOR = Color.BG_DARK
                self.widgets['textRemain'] = Text(self.window, self.cut.getPos(0, 24), self.cut.getSize(44, 2), (255, 255, 255), f"{i18n('remain')} :", 1, Anchor.RIGHT)
                self.widgets['remain'] = Text(self.window, self.cut.getPos(45, 24), self.cut.getSize(2, 2), Color.RARITY[0], str(len(self.objects) - self.objActual - 1))
                # self.widgets['object'].animations.append(JumpAnimation(self.widgets['object'], 10, 0.5))
                if self.objActual + 2 <= len(self.objects):
                    if Save.read(Save.getPath(self.objects[self.objActual + 1].kind, self.objects[self.objActual + 1].name)) == 1:
                        self.widgets['remain'].animations.append(FlashAnimation(self.widgets['remain'], 0.1, Color.RARITY[4]))

            if level == 1:
                self.loopNewObject(obj)
            else:
                self.loopUpgradeObject(obj, level)

        if Input.clic and self.canClick:
            del self.widgets['textRemain']
            del self.widgets['remain']
            if self.objActual + 2 > len(self.objects):
                self.nextScreen = 'menu'
            else:
                self.objActual += 1

    def loopNewObject(self, obj):
        if not self.widgets.get('object'):
            self.canClick = False
            self.widgets['object'] = Image(self.window, self.cut.getPos(23, 13), self.cut.getSize(2, 2), obj.image)
            self.widgets['object'].animations.append(ResizeAnimation(self.widgets['object'], 2, self.cut.getSize(18, 18)))
            self.widgets['object'].animations.append(LinearAnimation(self.widgets['object'], 2, self.cut.getPos(15, 5)))
        elif not self.widgets['object'].animations:
            self.canClick = True
            self.widgets['object'].animations.append(JumpAnimation(self.widgets['object'], 0.5, 10))
            self.widgets['title'] = Text(self.window, self.cut.getPos(14, 1), self.cut.getSize(20, 3), Color.RARITY[1], i18n(obj.kind, obj.name))
            self.widgets['title'].animations.append(FlashAnimation(self.widgets['title'], 0.1, Color.RARITY[4]))
            Rules.BG_COLOR = Color.RARITY[obj.rarity]

        if Input.clic and self.widgets.get('object') and self.widgets.get('title'):
            del self.widgets['title']
            del self.widgets['object']

    def loopUpgradeObject(self, obj, level):
        if not self.widgets.get('object'):
            self.canClick = False
            self.widgets['backgroundUpgrade'] = Rectangle(self.window, self.cut.getPos(27, 8), self.cut.getSize(15, 11), Color.BG_LIGHT)
            self.widgets['upgradeText'] = Text(self.window, self.cut.getPos(28, 9), self.cut.getSize(13, 3), Color.RARITY[0], i18n('upgrade'))
            self.widgets['infLevel'] = Text(self.window, self.cut.getPos(32, 13), self.cut.getSize(4, 5), Color.WHITE, str(level - 1))
            self.widgets['infLevel'].animations.append(
                LinearAnimation(self.widgets['infLevel'], 0.2, self.cut.getPos(28, 13), 1.01))
            self.widgets['supLevel'] = Text(self.window, self.cut.getPos(32, 13), self.cut.getSize(4, 5), Color.WHITE, str(level))
            self.widgets['supLevel'].animations.append(
                LinearAnimation(self.widgets['supLevel'], 0.2, self.cut.getPos(37, 13), 1.01))
            self.widgets['>>>'] = Text(self.window, self.cut.getPos(32, 14), self.cut.getSize(5, 3), Color.WHITE, '>>>')
            self.widgets['object'] = Image(self.window, self.cut.getPos(14, 5), self.cut.getSize(20, 17), obj.image)
            self.widgets['object'].animations.append(
                LinearAnimation(self.widgets['object'], 0.2, self.cut.getPos(6, 5), 1.01))
        elif not self.widgets['object'].animations:
            self.canClick = True
            self.widgets['object'].animations.append(JumpAnimation(self.widgets['object'], 0.5, 10))
            self.widgets['title'] = Text(self.window, self.cut.getPos(14, 1), self.cut.getSize(20, 3), (255, 255, 255), i18n(obj.kind, obj.name))
            self.widgets['title'].animations.append(FlashAnimation(self.widgets['title'], 0.1, Color.RARITY[obj.rarity]))
            self.widgets['upgradeText'].animations.append(JumpAnimation(self.widgets['upgradeText'], 0.5, 10))

        if Input.clic and self.widgets.get('object') and self.widgets.get('title'):
            del self.widgets['title']
            del self.widgets['object']
            del self.widgets['upgradeText']
            del self.widgets['infLevel']
            del self.widgets['supLevel']
            del self.widgets['backgroundUpgrade']
            del self.widgets['>>>']

    def draw(self):
        """
        Tirage au sort des nouveaux objets

        objects: tous les objets
        result: objets gagnés dans ce coffre
        """

        objects = list(Mob) + list(Effect)
        result = []

        # 3 nouveaux objets (moins si double tirage)
        for i in range(3):

            # objets pas encore débloqués
            newObjects = {rarity: [obj for obj in objects if obj.rarity == rarity and Save.read(Save.getPath(obj.kind, obj.name)) == 0] for rarity in [1, 2, 3, 4]}
            # objets améliorables
            upObjects = [obj for obj in objects if 0 < Save.read(Save.getPath(obj.kind, obj.name)) < 10]
            # objets améliorés au niveau maximum
            maxObjects = [obj for obj in objects if Save.read(Save.getPath(obj.kind, obj.name)) == 10]

            # vérifie si il n'y a plus d'objets à améliorer
            newObj = not upObjects and list(newObjects.values()) != [[], [], [], []]

            # essaie de débloquer un nouvel objet
            obj = self.drawNew(newObjects)
            # débloque inévitablement un nouvel objet si c'est le premier coffre
            while obj is None and newObj:
                obj = self.drawNew(newObjects)

            # sinon essaie d'améliorer un objet améliorable
            if obj is None and upObjects:
                obj = random.choice(upObjects)

            # si un objet a été choisi, mettre à jour les données
            if obj is not None and obj not in result:
                path = Save.getPath(obj.kind, obj.name)
                Save.write(path, Save.read(path) + 1)
                # nouveaux objets à la fin du coffre
                if obj in upObjects:
                    result.insert(0, obj)
                else:
                    result.append(obj)

        return result

    def drawNew(self, newObjects):
        """
        Essaie de débloquer un nouvel objet

        rd: nombre aléatoire entre 0 et 1
        obj: nouvel objet, sinon None
        """

        rd = random.random()
        obj = None
        for index, prob in enumerate(Rules.PROBS):
            if rd <= prob:
                if newObjects[index + 1]:
                    obj = random.choice(newObjects[index + 1])
                else:
                    obj = None
        return obj