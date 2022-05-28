from data.enum.colors import Color
from widget._widget import Widget
from widget.game.effect import EffectWidget
from widget.group import GroupWidget
from widget.image import Image
from widget.play.healthBar import HealthBar
from widget.rectangle import Rectangle


class InfoCardWidget(Widget):

    def __init__(self, window, position, size, mob, health, effects):
        super().__init__(window, position, size)

        hearts = mob.health if health is None else health
        if effects is None:
            effects = {}

        effectsWidget = GroupWidget(self.window, self.getPos(0, 0), self.getSize(2, 7),
                                    tuple([EffectWidget(self.window, self.getPos(0, y), self.getSize(2, 1), *effect)
                                           for y, effect in enumerate(effects.items())]))

        self.widget = GroupWidget(self.window, self.getPos(0, 0), self.getSize(4, 7), (
            Rectangle(self.window, self.getPos(3, 0), self.getSize(4, 7), Color.RARITY[mob.rarity]),
            Image(self.window, self.getPos(3.25, 0.25), self.getSize(3.5, 3.5), mob.image),
            Rectangle(self.window, self.getPos(3, 0), self.getSize(4, 7), Color.WHITE, 2),
            HealthBar(self.window, self.getPos(3.5, 4), self.getSize(3, 2.5), mob.health, (6, 5)).setHealth(hearts),
            effectsWidget
        ))

    def loop(self):
        super().loop()
        self.widget.loop()

    def setPosition(self, position):
        super().setPosition(position)
        self.widget.setPosition(position)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 7 * x), round(self.position[1] + self.size[1] / 7 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 7 * w), round(self.size[1] / 7 * h)
