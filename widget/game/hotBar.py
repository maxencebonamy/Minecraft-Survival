from data.enum.colors import Color
from data.enum.items import Item
from util.screenCutting import ScreenCutting
from widget._widget import Widget
from widget.group import GroupWidget
from widget.image import Image
from widget.play.item import ItemWidget
from widget.rectangle import Rectangle
from widget.text import Text


class HotBarWidget(Widget):

    def __init__(self, window, position, size):
        super().__init__(window, position, size)

        self.cut = ScreenCutting(48, 27)
        x, y = self.cut.getOriginPos(*position)
        self.coords = [(x + 2 * index, y) for index in range(9)]

        self.cases = {}

    def loop(self):
        super().loop()
        for case in self.cases.values():
            case.loop()

    def setCase(self, index, widget, *args):
        self.cases[index] = widget(self.window, self.cut.getPos(*self.coords[index - 1]), self.cut.getSize(2, 2), *args)
        if 'sword' in args[0].name or 'bow' == args[0].name or 'flint_and_steel' == args[0].name or \
                'golden_apple' == args[0].name:
            self.cases[index].setAnimSelect()

    def setHotBar(self, hotBar):
        for index, value in enumerate(hotBar.values()):
            if value[0] is None:
                self.setCase(index + 1, ItemWidget, Item.EMPTY, 0, 0)
            else:
                self.setCase(index + 1, ItemWidget, *value)
