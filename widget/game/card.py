from data.enum.colors import Color
from widget._widget import Widget
from widget.group import GroupWidget
from widget.image import Image
from widget.play.healthBar import HealthBar
from widget.rectangle import Rectangle


class CardWidget(Widget):

    def __init__(self, window, position, size, mob, health=None):
        super().__init__(window, position, size)

        self.mob = mob

        hearts = mob.health if health is None else health

        self.widget = GroupWidget(self.window, self.getPos(0, 0), self.getSize(4, 7), (
            Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 7), Color.RARITY[mob.rarity]),
            Image(self.window, self.getPos(0.25, 0.25), self.getSize(3.5, 3.5), mob.image),
            Rectangle(self.window, self.getPos(0, 0), self.getSize(4, 7), Color.WHITE, 2)
        ))

        self.healthBar = HealthBar(self.window, self.getPos(0.5, 4), self.getSize(3, 2.5), mob.health, (6, 5)).setHealth(hearts)

    def loop(self):
        super().loop()
        self.widget.loop()
        self.healthBar.loop()

    def setPosition(self, position):
        super().setPosition(position)
        self.widget.setPosition(position)
        self.healthBar.setPosition(self.getPos(0.5, 4))

    def damage(self, hearts=1):
        self.healthBar.damage(hearts)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 4 * x), round(self.position[1] + self.size[1] / 7 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 4 * w), round(self.size[1] / 7 * h)