import random

from data.enum.colors import Color
from data.enum.difficulties import Difficulty
from data.enum.effects import Effect
from data.enum.mobs import Mob
from game.game import Game
from game.rules import Rules
from i18n.i18n import i18n
from images import Import
from save import Save
from screen._screen import Screen
from util.anchor import Anchor
from widget.button import Button
from widget.collection.cover import Cover
from widget.group import GroupWidget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class PlayScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.BG_COLOR = Color.BG_DARK

        self.widgets = {
            'topLine': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), (255, 255, 255), 2),
            'bottomLine': Rectangle(self.window, self.cut.getPos(0, 23), self.cut.getSize(48, 0), (255, 255, 255), 2),

            'title': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n('play'), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),
            'playButton': Button(self.window, self.cut.getPos(16, 23.5), self.cut.getSize(16, 3), i18n('play')).setAnimSelect(),
        }

        if Rules.GAME_EFFECT is None:
            Rules.GAME_EFFECT = random.choice([effect for effect in Effect if Save.read(Save.getPath('effect', effect.name)) > 0])
        if Rules.GAME_MOB is None:
            Rules.GAME_MOB = random.choice([mob for mob in Mob if Save.read(Save.getPath('mob', mob.name)) > 0])

        self.widgets['effect'] = Cover(self.window, self.cut.getPos(37, 5), self.cut.getSize(10, 8), Rules.GAME_EFFECT).setAnimSelect()
        self.widgets['mob'] = Cover(self.window, self.cut.getPos(37, 14), self.cut.getSize(10, 8), Rules.GAME_MOB).setAnimSelect()

        if Rules.GAME_DIFFICULTY is None:
            Rules.GAME_DIFFICULTY = Difficulty.PEACEFUL

        self.widgets['properties'] = self.difficultyWidget()
        self.widgets['difficulty-'] = Text(self.window, self.cut.getPos(3, 5), self.cut.getSize(4, 3), Color.WHITE, '<').setAnimSelect()
        self.widgets['difficulty+'] = Text(self.window, self.cut.getPos(30, 5), self.cut.getSize(4, 3), Color.WHITE, '>').setAnimSelect()

    def loop(self):
        super().loop()

        if self.widgets['difficulty+'] in self.clicWidgets:
            Rules.GAME_DIFFICULTY = Difficulty.increase(Rules.GAME_DIFFICULTY)
            self.widgets['properties'] = self.difficultyWidget()
        elif self.widgets['difficulty-'] in self.clicWidgets:
            Rules.GAME_DIFFICULTY = Difficulty.decrease(Rules.GAME_DIFFICULTY)
            self.widgets['properties'] = self.difficultyWidget()
        elif self.widgets['effect'] in self.clicWidgets:
            Rules.KIND_SELECT = Effect
            self.nextScreen = 'objectChoice'
        elif self.widgets['mob'] in self.clicWidgets:
            Rules.KIND_SELECT = Mob
            self.nextScreen = 'objectChoice'

        elif self.widgets.get('closeButton') in self.clicWidgets:
            self.nextScreen = 'menu'
        elif self.widgets.get('playButton') in self.clicWidgets:
            Rules.GAME = Game(Rules.GAME_DIFFICULTY)
            Rules.GAME.effect = Rules.GAME_EFFECT
            Rules.GAME.items = Rules.GAME.setItems()
            self.nextScreen = 'gameCollect'

    def propertyWidget(self, y, name, value, image):
        return GroupWidget(self.window, self.cut.getPos(1, y), self.cut.getSize(35, 3), (
            Image(self.window, self.cut.getPos(2.5, y+0.5), self.cut.getSize(2, 2), image),
            Text(self.window, self.cut.getPos(6, y), self.cut.getSize(15, 3), Color.WHITE, name, 0.8, Anchor.LEFT),
            Text(self.window, self.cut.getPos(22, y), self.cut.getSize(12, 3), Color.RARITY[0], value, 0.8, Anchor.RIGHT),
        ))

    def difficultyWidget(self):
        return GroupWidget(self.window, self.cut.getPos(1, 5), self.cut.getSize(35, 17), (
            Rectangle(self.window, self.cut.getPos(1, 5), self.cut.getSize(35, 17), Color.WHITE, 2),
            Rectangle(self.window, self.cut.getPos(1, 8), self.cut.getSize(35, 0), Color.WHITE, 2),
            Text(self.window, self.cut.getPos(1, 5), self.cut.getSize(35, 3), Color.RARITY[1], i18n('difficulties', Rules.GAME_DIFFICULTY.name), 0.8),
            self.propertyWidget(9, i18n('steps'), str(Rules.GAME_DIFFICULTY.maxStep), Import.CHEST),
            self.propertyWidget(12, i18n('rounds'), str(Rules.GAME_DIFFICULTY.rounds), Import.ITEM.DIAMOND_SWORD),
            self.propertyWidget(15, i18n('emerald'), str(Rules.GAME_DIFFICULTY.emerald), Import.EMERALD),
            self.propertyWidget(18, i18n('attribute', 'trophy'), str(Rules.GAME_DIFFICULTY.trophies), Import.TROPHY),
        ))