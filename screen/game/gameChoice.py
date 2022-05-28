from data.enum.colors import Color
from game.rules import Rules
from i18n.i18n import i18n
from screen._screen import Screen
from widget.button import Button
from widget.play.item import ItemWidget
from widget.rectangle import Rectangle
from widget.text import Text


class GameChoiceScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.GAME.screen = 'gameChoice'

        Rules.BG_COLOR = Color.BG_DARK

        self.widgets = {
            # 'topBg': Rectangle(self.window, (0, 0), self.cut.getSize(48, 4), Color.BG_DARK),
            # 'bg': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 23), Color.BG_LIGHT),
            'topLine': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), Color.WHITE, 2),

            'title': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n('choice'), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),
        }

        x = 2
        for key, value in Rules.GAME.items[Rules.GAME.step].items():
            self.widgets[f'item{key.name}'] = ItemWidget(self.window, self.cut.getPos(x, 11), self.cut.getSize(8, 8), key, value).setAnimSelect()
            x += 12

    def loop(self):
        super().loop()

        if self.widgets['closeButton'] in self.clicWidgets:
            self.nextScreen = 'gameCollect'

        else:
            for widget in self.clicWidgets:
                if isinstance(widget, ItemWidget):
                    Rules.GAME.step += 1
                    Rules.GAME.inventory[widget.item] += widget.value
                    self.nextScreen = 'gameCollect'