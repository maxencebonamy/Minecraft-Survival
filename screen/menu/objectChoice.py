from data.enum.colors import Color
from data.enum.effects import Effect
from data.enum.mobs import Mob
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from save import Save
from screen._screen import Screen
from widget.button import Button
from widget.collection.cover import Cover
from widget.group import GroupWidget
from widget.rectangle import Rectangle
from widget.text import Text


class ObjectChoiceScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.BG_COLOR = Color.BG_DARK
        kind = Rules.KIND_SELECT

        self.widgets = {
            'topLine': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), (255, 255, 255), 2),
            'title': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n('title', kind.getKind()), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),
        }

        objects = [obj for obj in kind]
        coords = [(7 + 7 * x, 5 + 5.5 * y) for y in range(4) for x in range(5)]
        del coords[-1]
        self.covers = [
            Cover(self.window, self.cut.getPos(*position), self.cut.getSize(6, 4.5), objects[index]).setAnimSelect()
            for index, position in enumerate(coords)]

        self.widgets['cover'] = GroupWidget(self.window, self.cut.getPos(*coords[0]), self.cut.getSize(48, 23), self.covers)

    def loop(self):
        super().loop()

        if Input.clic:
            for cover in self.covers:
                if cover.isSelected():
                    if Save.read(Save.getPath(cover.name.kind, cover.name.name)) > 0:
                        if Rules.KIND_SELECT == Mob:
                            Rules.GAME_MOB = cover.name
                        elif Rules.KIND_SELECT == Effect:
                            Rules.GAME_EFFECT = cover.name
                        self.nextScreen = 'play'

        if self.widgets.get('closeButton') in self.clicWidgets:
            self.nextScreen = 'play'
