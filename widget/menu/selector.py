from data.enum.colors import Color
from widget._widget import Widget
from widget.rectangle import Rectangle


class Selector(Widget):

    def __init__(self, window, position, size, color=Color.BLACK):
        super().__init__(window, position, size)

        self.rectangle = Rectangle(window, position, size, color).setOpacity(100)
        self.outline = Rectangle(window, position, size, color, 2)

    def loop(self):
        super().loop()

        self.rectangle.loop()
        self.outline.loop()

    def setPosition(self, position):
        super().setPosition(position)

        self.rectangle.setPosition(position)
        self.outline.setPosition(position)