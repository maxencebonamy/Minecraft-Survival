import random

from data.enum.colors import colors, Color
from data.enum.effects import Effect
from game.rules import Rules
from i18n.i18n import i18n
from images import Import
from data.enum.mobs import Mob
from input.input import Input
from output.sound import Sound
from save import Save
from screen._screen import Screen
from widget.button import Button
from widget.collection.cover import Cover
from widget.image import Image
from widget.menu.property import Property
from widget.rectangle import Rectangle
from widget.text import Text


class MenuScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.BG_COLOR = Color.FG_DARK

        self.getFirstObjects()

        self.widgets = {
            # background
            # 'ccBg': Rectangle(self.window, self.cut.getPos(15, 10), self.cut.getSize(18, 11), colors['light']['f']),
            # 'csBg': Rectangle(self.window, self.cut.getPos(15, 21), self.cut.getSize(18, 6), colors['light']['b']),
            # 'cnBg': Rectangle(self.window, self.cut.getPos(15, 0), self.cut.getSize(18, 10), colors['light']['b']),
            #
            # 'wcBg': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(15, 19), colors['dark']['f']),
            # 'wsBg': Rectangle(self.window, self.cut.getPos(0, 23), self.cut.getSize(15, 4), colors['dark']['b']),
            # 'wnBg': Rectangle(self.window, self.cut.getPos(0, 0), self.cut.getSize(15, 4), colors['dark']['b']),
            #
            # 'ecBg': Rectangle(self.window, self.cut.getPos(33, 4), self.cut.getSize(15, 19), colors['dark']['f']),
            # 'esBg': Rectangle(self.window, self.cut.getPos(33, 23), self.cut.getSize(15, 4), colors['dark']['b']),
            # 'enBg': Rectangle(self.window, self.cut.getPos(33, 0), self.cut.getSize(15, 4), colors['dark']['b']),

            # sep
            'leftSep': Rectangle(self.window, self.cut.getPos(15, 0), self.cut.getSize(0, 27), (255, 255, 255), 2),
            'rightSep': Rectangle(self.window, self.cut.getPos(33, 0), self.cut.getSize(0, 27), (255, 255, 255), 2),
            'leftTopSep': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(15, 0), (255, 255, 255), 2),
            'leftBottomSep': Rectangle(self.window, self.cut.getPos(0, 23), self.cut.getSize(15, 0), (255, 255, 255), 2),
            'rightTopSep': Rectangle(self.window, self.cut.getPos(33, 4), self.cut.getSize(15, 0), (255, 255, 255), 2),
            'rightBottomSep': Rectangle(self.window, self.cut.getPos(33, 23), self.cut.getSize(15, 0), (255, 255, 255), 2),
            'centerTopSep': Rectangle(self.window, self.cut.getPos(15, 10), self.cut.getSize(18, 0), (255, 255, 255), 2),
            'centerBottomSep': Rectangle(self.window, self.cut.getPos(15, 21), self.cut.getSize(18, 0), (255, 255, 255), 2),

            # center
            'playButton': Button(self.window, self.cut.getPos(16, 22), self.cut.getSize(16, 4), i18n('play')).setAnimSelect(),
            'emerald': Property(self.window, self.cut.getPos(16, 7), self.cut.getSize(16, 2), str(Save.read(Save.getPath('emerald'))), Import.EMERALD),
            'trophies': Property(self.window, self.cut.getPos(16, 4), self.cut.getSize(16, 2), self.getTotalTrophies(), Import.TROPHY).setAnimSelect(),
            'settings': Property(self.window, self.cut.getPos(16, 1), self.cut.getSize(16, 2), i18n('settings'), Import.SETTINGS).setAnimSelect(),
            'chest': Image(self.window, self.cut.getPos(20, 11), self.cut.getSize(8, 9), Import.CHEST).setAnimSelect(),

            # left
            'effectLeftButton': Button(self.window, self.cut.getPos(1, 24), self.cut.getSize(6, 2), '<<<').setAnimSelect(),
            'effectRightButton': Button(self.window, self.cut.getPos(8, 24), self.cut.getSize(6, 2), '>>>').setAnimSelect(),
            'effectText': Text(self.window, self.cut.getPos(1, 1), self.cut.getSize(13, 2), (255, 255, 255), i18n('title', 'effect')),

            # right
            'mobLeftButton': Button(self.window, self.cut.getPos(34, 24), self.cut.getSize(6, 2), '<<<').setAnimSelect(),
            'mobRightButton': Button(self.window, self.cut.getPos(41, 24), self.cut.getSize(6, 2), '>>>').setAnimSelect(),
            'mobText': Text(self.window, self.cut.getPos(34, 1), self.cut.getSize(13, 2), (255, 255, 255), i18n('title', 'mob')),
        }

        self.mobLeft, self.mobRight = 34, 41
        self.effectLeft, self.effectRight = 1, 8

        self.updateWidgets(self.mobLeft, self.mobRight, Mob, Rules.MOB_RARITY)
        self.updateWidgets(self.effectLeft, self.effectRight, Effect, Rules.EFFECT_RARITY)

    def loop(self):
        super().loop()
        if Input.clic:
            if self.widgets.get('chest') in self.clicWidgets:
                self.nextScreen = 'chest'
            elif self.widgets.get('playButton') in self.clicWidgets:
                self.nextScreen = 'play'
            elif self.widgets.get('settings') in self.clicWidgets:
                self.nextScreen = 'settings'
            elif self.widgets.get('trophies') in self.clicWidgets:
                self.nextScreen = 'trophies'
            elif self.widgets.get('mobLeftButton') in self.clicWidgets:
                Rules.MOB_RARITY -= 1
                self.updateWidgets(self.mobLeft, self.mobRight, Mob, Rules.MOB_RARITY)
            elif self.widgets.get('mobRightButton') in self.clicWidgets:
                Rules.MOB_RARITY += 1
                self.updateWidgets(self.mobLeft, self.mobRight, Mob, Rules.MOB_RARITY)
            elif self.widgets.get('effectLeftButton') in self.clicWidgets:
                Rules.EFFECT_RARITY -= 1
                self.updateWidgets(self.effectLeft, self.effectRight, Effect, Rules.EFFECT_RARITY)
            elif self.widgets.get('effectRightButton') in self.clicWidgets:
                Rules.EFFECT_RARITY += 1
                self.updateWidgets(self.effectLeft, self.effectRight, Effect, Rules.EFFECT_RARITY)
            else:
                for widget in self.clicWidgets:
                    if isinstance(widget, Cover):
                        Rules.NAME_SELECT = widget.name
                        if isinstance(widget.name, Mob):
                            self.nextScreen = 'mobProfile'
                        elif isinstance(widget.name, Effect):
                            self.nextScreen = 'effectProfile'

    def updateWidgets(self, left, right, kind, rarity):
        kindStr = ''
        for i in kind:
            kindStr = i.kind

        for i in range(6):
            if f'{kindStr}{i}' in self.widgets.keys():
                del self.widgets[f'{kindStr}{i}']

        self.widgets[f'{kindStr}LeftButton'] = Button(self.window, self.cut.getPos(left, 24), self.cut.getSize(6, 2), '<<<').setAnimSelect()
        self.widgets[f'{kindStr}RightButton'] = Button(self.window, self.cut.getPos(right, 24), self.cut.getSize(6, 2), '>>>').setAnimSelect()

        if rarity <= 1:
            del self.widgets[f'{kindStr}LeftButton']
        elif rarity >= 4:
            del self.widgets[f'{kindStr}RightButton']

        disp = [value for value in kind if value.rarity == rarity]

        i = 0
        for y in range(5, 18, 6):
            for x in range(left, right + 1, 7):
                if i < len(disp):
                    self.widgets[f'{kindStr}{i}'] = Cover(self.window, self.cut.getPos(x, y), self.cut.getSize(6, 5), disp[i]).setAnimSelect()
                    i += 1

    def getFirstObjects(self):
        mobs = [mob for mob in Mob if Save.read(Save.getPath('mob', mob.name)) > 0]
        effects = [effect for effect in Effect if Save.read(Save.getPath('effect', effect.name)) > 0]

        if not mobs and not effects:
            mob = random.choice([mob for mob in Mob if mob.rarity == 1])
            effect = random.choice([effect for effect in Effect if effect.rarity == 1])

            Save.write(Save.getPath('mob', mob.name), int(Save.read(Save.getPath('mob', mob.name)) + 1))
            Save.write(Save.getPath('effect', effect.name), int(Save.read(Save.getPath('effect', effect.name)) + 1))

    def getTotalTrophies(self):
        trophy = 0
        for obj in list(Mob) + list(Effect):
            trophy += Save.read(Save.getPath('trophies', obj.name))
        return str(trophy)