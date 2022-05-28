from data.enum.colors import Color
from widget._widget import Widget
from widget.group import GroupWidget
from widget.image import Image
from widget.rectangle import Rectangle


class MovePlayerWidget(Widget):

    def __init__(self, window, position, size, mob):
        super().__init__(window, position, size)

        self.widget = GroupWidget(self.window, self.getPos(0, 0), self.getSize(4, 7), (
            Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 7), Color.GRAY),
            Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 7), Color.WHITE, 2),
            Image(self.window, self.getPos(0.25, 0.25), self.getSize(3.5, 6.5), mob.image),
            Rectangle(self.window, self.getPos(0.25, 0.25), self.getSize(3.5, 6.5), Color.GRAY).setOpacity(180),
        ))

    def loop(self):
        super().loop()
        self.widget.loop()

    def setPosition(self, position):
        super().setPosition(position)
        self.widget.setPosition(position)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 4 * x), round(self.position[1] + self.size[1] / 7 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 4 * w), round(self.size[1] / 7 * h)