from data.enum.colors import Color
from data.enum.effects import Effect
from data.enum.mobs import Mob
from game.rules import Rules
from i18n.i18n import i18n
from images import Import
from input.input import Input
from save import Save
from screen._screen import Screen
from widget.button import Button
from widget.group import GroupWidget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class TrophiesScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.BG_COLOR = Color.BG_DARK

        self.widgets = {
            'topOutline': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), (255, 255, 255), 2),

            'title': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n('trophies'), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),
        }

        totalTrophies = self.getTotalTrophies()

        coords = [(2 + 5*x, 6 + 5*y) for y in range(4) for x in range(9)]
        self.trophies = {
            10: 100,
            25: 50,
            50: 50,
            100: 100,
            125: 50,
            150: 50,
            175: 50,
            200: 100,
            250: 50,
            300: 100,
            400: 50,
            500: 100,
            600: 50,
            700: 50,
            800: 50,
            900: 50,
            1000: 100,
            1250: 50,
            1500: 100,
            1750: 50,
            2000: 100,
            2500: 50,
            3000: 100,
            4000: 100,
            5000: 150,
            6000: 100,
            7000: 100,
            8000: 100,
            9000: 100,
            10000: 200,
            12500: 100,
            15000: 150,
            17500: 100,
            20000: 200,
            25000: 100,
            30000: 200,
        }

        for index, reward in enumerate(self.trophies.items()):
            trophy, emerald = reward
            x, y = coords[index]
            if totalTrophies >= trophy:
                self.widgets[str(index)] = GroupWidget(window, self.cut.getPos(x, y), self.cut.getSize(4, 4), (
                    Rectangle(window, self.cut.getPos(x, y), self.cut.getSize(4, 2), Color.RARITY[2]),
                    Rectangle(window, self.cut.getPos(x, y + 2), self.cut.getSize(4, 2), Color.RARITY[3]),
                    Image(window, self.cut.getPos(x + 0.25, y + 0.1), self.cut.getSize(1, 1.8), Import.TROPHY),
                    Text(window, self.cut.getPos(x + 1.5, y), self.cut.getSize(2.5, 2), Color.WHITE, str(trophy), 0.7),
                    Image(window, self.cut.getPos(x + 0.25, y + 2.1), self.cut.getSize(1, 1.8), Import.EMERALD),
                    Text(window, self.cut.getPos(x + 1.5, y + 2), self.cut.getSize(2.5, 2), Color.WHITE, str(emerald), 0.7),
                    Rectangle(window, self.cut.getPos(x, y), self.cut.getSize(4, 4), Color.WHITE, 2),
                    Rectangle(window, self.cut.getPos(x, y + 2), self.cut.getSize(4, 0), Color.WHITE, 2)
                ))
                if Save.read(Save.getPath('rewards', str(index + 1))) == 0:
                    self.widgets[str(index)].setAnimSelect()
            else:
                self.widgets[str(index)] = GroupWidget(window, self.cut.getPos(x, y), self.cut.getSize(4, 4), (
                    Rectangle(window, self.cut.getPos(x, y), self.cut.getSize(4, 2), Color.FG_DARK),
                    Rectangle(window, self.cut.getPos(x, y + 2), self.cut.getSize(4, 2), Color.BG_LIGHT),
                    Image(window, self.cut.getPos(x + 0.25, y + 0.1), self.cut.getSize(1, 1.8), Import.TROPHY),
                    Text(window, self.cut.getPos(x + 1.5, y), self.cut.getSize(2.5, 2), Color.WHITE, str(trophy), 0.7),
                    Image(window, self.cut.getPos(x + 0.25, y + 2.1), self.cut.getSize(1, 1.8), Import.EMERALD),
                    Text(window, self.cut.getPos(x + 1.5, y + 2), self.cut.getSize(2.5, 2), Color.WHITE, str(emerald), 0.7),
                    Rectangle(window, self.cut.getPos(x, y), self.cut.getSize(4, 4), Color.WHITE, 2),
                    Rectangle(window, self.cut.getPos(x, y + 2), self.cut.getSize(4, 0), Color.WHITE, 2)
                ))

    def loop(self):
        super().loop()

        if self.widgets.get('closeButton') in self.clicWidgets:
            self.nextScreen = 'menu'

        for name, widget in self.widgets.items():
            if name != 'closeButton' and widget.isSelected() and widget.playAnimWhenSelect and Input.clic:
                index = int(name)
                Save.write(Save.getPath('rewards', str(index+1)), 1)
                Save.write(Save.getPath('emerald'), Save.read(Save.getPath('emerald')) + list(self.trophies.values())[index])
                self.__init__(self.window)

    @staticmethod
    def getTotalTrophies():
        return sum(
            Save.read(Save.getPath('trophies', obj.name))
            for obj in list(Mob) + list(Effect)
        )