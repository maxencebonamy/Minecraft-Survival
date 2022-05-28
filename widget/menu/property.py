from data.enum.colors import Color
from util.anchor import Anchor
from widget._widget import Widget
from widget.group import GroupWidget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class Property(Widget):

    def __init__(self, window, position, size, text, image):
        super().__init__(window, position, size)

        self.widget = GroupWidget(window, position, size, (
            Rectangle(self.window, self.getPos(0, 0), self.getSize(16, 2), Color.BG_DARK),
            Image(self.window, self.getPos(1.25, 0.25), self.getSize(1.5, 1.5), image),
            Text(self.window, self.getPos(4, 0), self.getSize(11, 2), (255, 255, 255), text, 0.8, Anchor.RIGHT),
            Rectangle(self.window, self.getPos(0, 0), self.getSize(16, 2), (255, 255, 255), 2)
        ))

    def loop(self):
        super().loop()

        self.widget.loop()

    def setPosition(self, position):
        super().setPosition(position)

        self.widget.setPosition(position)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 16 * x), round(self.position[1] + self.size[1] / 2 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 16 * w), round(self.size[1] / 2 * h)