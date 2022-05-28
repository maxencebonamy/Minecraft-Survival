from data.enum.colors import Color
from game.rules import Rules
from i18n.i18n import i18n
from images import Import
from save import Save
from screen._screen import Screen
from widget.button import Button
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class ChestScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.BG_COLOR = Color.BG_DARK

        self.widgets = {
            # 'topBg': Rectangle(self.window, (0, 0), self.cut.getSize(48, 4), Color.BG_DARK),
            # 'bg': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 23), Color.BG_LIGHT),
            'topOutline': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), (255, 255, 255), 2),

            'title': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n('chest'), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),

            'emeraldOutline': Rectangle(self.window, self.cut.getPos(38, 1), self.cut.getSize(8, 2), (255, 255, 255), 2),
            'emeraldText': Text(self.window, self.cut.getPos(40, 1), self.cut.getSize(6, 2), (255, 255, 255), str(Rules.CHEST_COST)),
            'emerald': Image(self.window, self.cut.getPos(38.2, 1.2), self.cut.getSize(1.6, 1.6), Import.EMERALD),

            'chest': Image(self.window, self.cut.getPos(10, 5), self.cut.getSize(28, 17), Import.CHEST),
            'buyButton': Button(self.window, self.cut.getPos(18, 23), self.cut.getSize(12, 3), i18n('buy')).setAnimSelect(),
        }

    def loop(self):
        super().loop()

        if self.widgets.get('closeButton') in self.clicWidgets:
            self.nextScreen = 'menu'
        elif self.widgets.get('buyButton') in self.clicWidgets:
            emerald = Save.read(Save.getPath('emerald'))
            if emerald >= Rules.CHEST_COST:
                Save.write(Save.getPath('emerald'), emerald - Rules.CHEST_COST)
                self.nextScreen = 'openChest'