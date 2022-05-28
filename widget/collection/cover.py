from animation.flash import FlashAnimation
from data.enum.colors import Color
from i18n.i18n import i18n
from images import Import
from save import Save
from widget._widget import Widget
from widget.group import GroupWidget
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class Cover(Widget):

    def __init__(self, window, position, size, name):
        super().__init__(window, position, size)

        self.name = name

        image = self.name.image
        level = Save.read(Save.getPath(self.name.kind, self.name.name))
        if level == 0:
            color = Color.GRAY
        else:
            color = Color.RARITY[self.name.rarity]

        text = str(level) if level != 0 else ''
        colorText = Color.WHITE if level != 10 else Color.RARITY[0]
        trophyText = str(Save.read(Save.getPath('trophies', self.name.name))) if level != 0 else ''
        trophyImage = Import.TROPHY if level != 0 else Import.EMPTY

        self.widget = GroupWidget(self.window, self.position, self.size, (
            Rectangle(window, self.getPos(0, 0), self.getSize(6, 4), color),
            Rectangle(window, self.getPos(0, 0), self.getSize(6, 4), Color.WHITE, 2),
            Image(window, self.getPos(0.25, 0.25), self.getSize(5.5, 3.5), image),
            Text(window, self.getPos(0.35, 0.1), self.getSize(2, 2), Color.BLACK, text, 0.8),
            Text(window, self.getPos(0.25, 0), self.getSize(2, 2), colorText, text, 0.8),
            Rectangle(window, self.getPos(0, 4), self.getSize(6, 1), color),
            Rectangle(window, self.getPos(0, 4), self.getSize(6, 1), Color.WHITE, 2),
            Image(window, self.getPos(1.1, 4.1), self.getSize(0.8, 0.8), trophyImage),
            Text(window, self.getPos(1.5, 4), self.getSize(3, 1), Color.WHITE, trophyText, 0.9)
        ))

    def loop(self):
        super().loop()

        self.widget.loop()

    def setPosition(self, position):
        super().setPosition(position)

        self.widget.setPosition(position)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 6 * x), round(self.position[1] + self.size[1] / 5 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 6 * w), round(self.size[1] / 5 * h)