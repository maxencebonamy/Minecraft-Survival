import random
from enum import Enum

from images import Import


class Effect(Enum):

    # NAME = name, rarity, onSelf, uses, duration, image

    BLOW_UP = ('blow_up', 1, True, 5, 1, Import.EFFECT.BLOW_UP)
    NAUSEA = ('nausea', 1, False, 15, 3, Import.EFFECT.NAUSEA)
    JUMP_BOOST = ('jump_boost', 1, True, 15, 1, Import.EFFECT.JUMP_BOOST)
    SPEED = ('speed', 1, True, 10, 1, Import.EFFECT.SPEED)
    BLINDNESS = ('blindness', 1, False, 10, 3, Import.EFFECT.BLINDNESS)
    WEAKNESS = ('weakness', 1, False, 15, 3, Import.EFFECT.WEAKNESS)

    FIRE = ('fire', 2, False, 15, 3, Import.EFFECT.FIRE)
    INVISIBILITY = ('invisibility', 2, True, 5, 1, Import.EFFECT.INVISIBILITY)
    INSTANT_DAMAGE = ('instant_damage', 2, False, 15, 1, Import.EFFECT.INSTANT_DAMAGE)
    FIRE_RESISTANCE = ('fire_resistance', 2, True, 15, 3, Import.EFFECT.FIRE_RESISTANCE)
    HASTE = ('haste', 2, True, 0, 0, Import.EFFECT.HASTE)

    TELEPORT = ('teleport', 3, True, 5, 1, Import.EFFECT.TELEPORT)
    POISON = ('poison', 3, False, 5, 3, Import.EFFECT.POISON)
    INSTANT_HEALTH = ('instant_health', 3, True, 10, 1, Import.EFFECT.INSTANT_HEALTH)
    ABSORPTION = ('absorption', 3, True, 10, 1, Import.EFFECT.ABSORPTION)

    RESISTANCE = ('resistance', 4, True, 15, 2, Import.EFFECT.RESISTANCE)
    LUCK = ('luck', 4, True, 0, 0, Import.EFFECT.LUCK)
    STRENGTH = ('strength', 4, True, 15, 3, Import.EFFECT.STRENGTH)
    REGENERATION = ('regeneration', 4, True, 15, 3, Import.EFFECT.REGENERATION)

    @property
    def name(self):
        return self.value[0]

    @property
    def rarity(self):
        return self.value[1]

    @property
    def onSelf(self):
        return self.value[2]

    @property
    def uses(self):
        return self.value[3]

    @property
    def duration(self):
        return self.value[4]

    @property
    def image(self):
        return self.value[5]

    @property
    def kind(self):
        return 'effect'

    @staticmethod
    def sort(rarity=None):
        if rarity is None:
            return random.choice([effect for effect in Effect])
        return random.choice([effect for effect in Effect if effect.rarity == rarity])

    @staticmethod
    def getKind():
        return 'effect'