from data.enum.colors import Color
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from widget._widget import Widget
from widget.button import Button
from widget.play.item import ItemWidget
from widget.rectangle import Rectangle
from widget.text import Text


class ChoiceWidget(Widget):

    def __init__(self, window, cut):
        super().__init__(window, (0, 0), Rules.SCREEN_SIZE)

        self.widgets = {
            'bg': Rectangle(self.window, (0, 0), Rules.SCREEN_SIZE, Color.BLACK).setOpacity(150),

            'title': Text(self.window, cut.getPos(10, 0), cut.getSize(28, 4), (255, 255, 255), i18n('choice'), 0.8),
            'closeButton': Button(self.window, cut.getPos(1, 1), cut.getSize(8, 2), '<<<').setAnimSelect(),
        }

        x = 8
        for key, value in Rules.GAME.items[Rules.GAME.step].items():
            self.widgets[f'item{key.name}'] = ItemWidget(self.window, cut.getPos(x, 5), cut.getSize(12, 16), key, value).setAnimSelect()
            x += 20

    def loop(self):
        super().loop()

        for widget in self.widgets.values():
            widget.loop()

        if Input.clic:
            if self.widgets['closeButton'].isSelected():
                del self

            else:
                for widget in self.widgets:
                    if isinstance(widget, ItemWidget) and widget.isSelected():
                        Rules.GAME.step += 1
                        Rules.GAME.inventory[widget.item] += widget.value
                        self.nextScreen = 'gameCollect'