from animation.flash import FlashAnimation
from data.enum.colors import Color
from widget._widget import Widget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class ItemWidget(Widget):

    def __init__(self, window,  position, size, item, value=None, level=None):
        super().__init__(window, position, size)

        # size = (3, 3)

        self.item = item

        self.value = value
        self.level = level

        color = Color.GRAY if value is not None and value == 0 else item.color

        self.widgets = {
            'bg': Rectangle(self.window, self.getPos(0, 0), self.getSize(3, 3), color),

            'image': Image(self.window, self.getPos(0.25, 0.25), self.getSize(2.5, 2.5), item.image),

            'outline': Rectangle(self.window, self.getPos(0, 0), self.getSize(3, 3), Color.WHITE, 2),
        }

        if value is not None and value > 1:
            self.widgets['shadowCount'] = Text(self.window, self.getPos(2.08, 2.08), self.getSize(1, 1), Color.BLACK, str(self.value), 1.1)
            self.widgets['count'] = Text(self.window, self.getPos(2, 2), self.getSize(1, 1), Color.WHITE, str(self.value), 1.1)

        if level is not None and level > 0:
            ch = (' I', ' II', ' III', ' IV', ' V')
            self.widgets['shadowLevel'] = Text(self.window, self.getPos(0.08, 0.08), self.getSize(1, 1), Color.BLACK, ch[self.level - 1], 1.1)
            self.widgets['level'] = Text(self.window, self.getPos(0, 0), self.getSize(1, 1), Color.WHITE, ch[self.level - 1], 1.1)
            self.widgets['level'].animations.append(FlashAnimation(self.widgets['level'], 0.1, Color.RARITY[0]))

    def loop(self):
        super().loop()

        for widget in self.widgets.values():
            widget.loop()

    def setPosition(self, position):
        super().setPosition(position)

        self.widgets['bg'].setPosition(self.getPos(0, 0))
        self.widgets['image'].setPosition(self.getPos(0.25, 0.25))
        self.widgets['outline'].setPosition(self.getPos(0, 0))

        if self.value is not None and self.value > 1:
            self.widgets['shadowCount'].setPosition(self.getPos(2.08, 2.08))
            self.widgets['count'].setPosition(self.getPos(2, 2))

        if self.level is not None and self.level > 0:
            self.widgets['shadowLevel'].setPosition(self.getPos(0.08, 0.08))
            self.widgets['level'].setPosition(self.getPos(0, 0))

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 3 * x), round(self.position[1] + self.size[1] / 3 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 3 * w), round(self.size[1] / 3 * h)