from data.enum.colors import Color
from i18n.i18n import i18n
from util.anchor import Anchor
from widget._widget import Widget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class Attribute(Widget):

    def __init__(self, window, position, size, name, value, path='attribute', plus=0):
        super().__init__(window, position, size)

        self.name = name
        self.value = value

        self.widgets = {
            'bg': Rectangle(self.window, self.getPos(3, 0), self.getSize(21, 2), Color.FG_DARK),

            'logo': Image(self.window, self.getPos(0, 0), self.getSize(2, 2), self.name.image),
            'text': Text(self.window, self.getPos(4, 0), self.getSize(11, 2), (255, 255, 255), i18n(path, self.name.name)).setAnchor(Anchor.LEFT),

            'outline': Rectangle(self.window, self.getPos(3, 0), self.getSize(21, 2), (255, 255, 255), 2),
        }

        if plus > 0:
            self.widgets['valuePlus'] = Text(self.window, self.getPos(19.5, 0), self.getSize(3.5, 2), Color.RARITY[0], f'+ {plus}').setAnchor(Anchor.CENTER)
            self.widgets['value'] = Text(self.window, self.getPos(16, 0), self.getSize(3.5, 2), (255, 255, 255), str(self.value)).setAnchor(Anchor.RIGHT)
        else:
            self.widgets['value'] = Text(self.window, self.getPos(16, 0), self.getSize(7, 2), (255, 255, 255), str(self.value)).setAnchor(Anchor.RIGHT)

    def loop(self):
        super().loop()

        for widget in self.widgets.values():
            widget.loop()

    def setPosition(self, position):
        super().setPosition(position)

        self.widgets['bg'].setPosition(self.getPos(0, 0))
        self.widgets['logo'].setPosition(self.getPos(0, 0))
        self.widgets['text'].setPosition(self.getPos(3, 0))
        self.widgets['value'].setPosition(self.getPos(16, 0))
        self.widgets['outline'].setPosition(self.getPos(0, 0))

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 24 * x), round(self.position[1] + self.size[1] / 2 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 24 * w), round(self.size[1] / 2 * h)