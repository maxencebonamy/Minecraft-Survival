from enum import Enum

from images import Import


class ObjectAttribute(Enum):

    # NAME = ('name', image)

    RARITY = ('rarity', Import.ATTRIBUTE.RARITY)
    LEVEL = ('level', Import.ATTRIBUTE.LEVEL)
    TARGET = ('target', Import.ATTRIBUTE.TARGET)
    USES = ('uses', Import.ATTRIBUTE.USES)
    HEALTH = ('health', Import.ATTRIBUTE.HEALTH)
    DAMAGE = ('damage', Import.ATTRIBUTE.DAMAGE)
    DISTANCE = ('distance', Import.ATTRIBUTE.DISTANCE)
    DURATION = ('duration', Import.ATTRIBUTE.DURATION)

    @property
    def name(self):
        return self.value[0]

    @property
    def image(self):
        return self.value[1]