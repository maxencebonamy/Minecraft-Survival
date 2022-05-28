from data.enum.colors import Color
from util.anchor import Anchor
from widget._widget import Widget
from widget.group import GroupWidget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class EffectWidget(Widget):

    def __init__(self, window, position, size, effect, duration):
        super().__init__(window, position, size)

        if duration < 0:
            text = GroupWidget(window, self.getPos(2, 0), self.getSize(2, 2), (
                Text(self.window, self.getPos(2.3, 0), self.getSize(1, 2), Color.WHITE, 'o', 0.8, Anchor.RIGHT),
                Text(self.window, self.getPos(3, 0), self.getSize(1, 2), Color.WHITE, 'o', 0.8, Anchor.LEFT)
            ))
        else:
            text = Text(self.window, self.getPos(2, 0), self.getSize(2, 2), Color.WHITE, str(duration), 0.8)

        self.widget = GroupWidget(self.window, self.getPos(0, 0), self.getSize(4, 2), (
            Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 2), Color.RARITY[effect.rarity]),
            Image(self.window, self.getPos(0.25, 0.25), self.getSize(1.5, 1.5), effect.image),
            text,
            Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 2), Color.WHITE, 2),
        ))

    def loop(self):
        super().loop()
        self.widget.loop()

    def setPosition(self, position):
        super().setPosition(position)
        self.widget.setPosition(position)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 4 * x), round(self.position[1] + self.size[1] / 2 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 4 * w), round(self.size[1] / 2 * h)