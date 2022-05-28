from data.enum.colors import Color
from game.rules import Rules
from data.enum.items import Item
from widget._widget import Widget
from widget.image import Image
from widget.rectangle import Rectangle


class TableWidget(Widget):

    def __init__(self, window, position, size, table):
        super().__init__(window, position, size)

        # size = (4, 4)

        self.playAnimWhenSelect = table.name == 'inventory' or Rules.GAME.inventory[Item.getItemByName(table.name)] > 0

        if self.playAnimWhenSelect:
            color = Color.FG_LIGHT
        else:
            color = Color.FG_DARK

        self.widgets = {
            'bg': Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 4), Color.FG_DARK),
            'image': Image(self.window, self.getPos(0.25, 0.25), self.getSize(3.5, 3.5), table.image),
            'outline': Rectangle(self.window, self.getPos(4, 0), self.getSize(0, 4), Color.WHITE, 2),
        }

    def loop(self):
        super().loop()

        for widget in self.widgets.values():
            widget.loop()

    def setPosition(self, position):
        super().setPosition(position)

        self.widgets['image'].setPosition(self.getPos(0.25, 0.25))

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 4 * x), round(self.position[1] + self.size[1] / 4 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 4 * w), round(self.size[1] / 4 * h)