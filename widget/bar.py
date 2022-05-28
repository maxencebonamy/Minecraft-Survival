from data.enum.colors import Color
from widget._widget import Widget
from widget.rectangle import Rectangle
from widget.text import Text


class Bar(Widget):

    def __init__(self, window, position, size, percent):
        super().__init__(window, position, size)

        self.outline = Rectangle(window, position, size, (255, 255, 255), 2)

        sizeBar = (self.w * percent, self.h)
        self.bar = Rectangle(window, position, sizeBar, Color.RARITY[2])

        self.text = Text(window, position, size, (255, 255, 255), f'{str(int(percent * 100))} %')

    def loop(self):
        self.bar.loop()
        self.outline.loop()
        self.text.loop()

    def setPosition(self, position):
        pass