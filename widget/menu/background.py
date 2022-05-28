from game.rules import Rules
from widget._widget import Widget
from widget.polygon import Polygon


class Background(Widget):

    def __init__(self, window):
        self.window = window
        self.size = Rules.SCREEN_SIZE

        super().__init__(window, (0, 0), self.size)

        self.polygons = [Polygon(self.window, (0, 0, 0), (
            (x, y), (x+30, y-20), (x+60, y), (x+60, y+35), (x+30, y+55), (x, y+35)
        )) for x in range(0, self.size[0], 150) for y in range(0, self.size[1], 150)]

    def loop(self):
        super().loop()

        for polygon in self.polygons:
            polygon.loop()