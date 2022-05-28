from enum import Enum


class Level(Enum):
    FLINT_AND_STEEL = ('flint_and_steel', 1, 1, 'duration')

    BOW = ('bow', 4, 1, 'damage')
    WOODEN_SWORD = ('wooden_sword', 4, 1, 'damage')
    GOLDEN_SWORD = ('golden_sword', 5, 1, 'damage')
    IRON_SWORD = ('iron_sword', 6, 1, 'damage')
    DIAMOND_SWORD = ('diamond_sword', 7, 1, 'damage')

    LEATHER_HELMET = ('leather_helmet', 0.8, -0.05, 'armor')
    LEATHER_CHESTPLATE = ('leather_chestplate', 0.6, -0.05, 'armor')
    LEATHER_LEGGINGS = ('leather_leggings', 0.7, -0.05, 'armor')
    LEATHER_BOOTS = ('leather_boots', 0.9, -0.05, 'armor')
    GOLDEN_HELMET = ('golden_helmet', 0.7, -0.05, 'armor')
    GOLDEN_CHESTPLATE = ('golden_chestplate', 0.5, -0.05, 'armor')
    GOLDEN_LEGGINGS = ('golden_leggings', 0.6, -0.05, 'armor')
    GOLDEN_BOOTS = ('golden_boots', 0.8, -0.05, 'armor')
    IRON_HELMET = ('iron_helmet', 0.6, -0.05, 'armor')
    IRON_CHESTPLATE = ('iron_chestplate', 0.4, -0.05, 'armor')
    IRON_LEGGINGS = ('iron_leggings', 0.5, -0.05, 'armor')
    IRON_BOOTS = ('iron_boots', 0.7, -0.05, 'armor')
    DIAMOND_HELMET = ('diamond_helmet', 0.5, -0.05, 'armor')
    DIAMOND_CHESTPLATE = ('diamond_chestplate', 0.3, -0.05, 'armor')
    DIAMOND_LEGGINGS = ('diamond_leggings', 0.4, -0.05, 'armor')
    DIAMOND_BOOTS = ('diamond_boots', 0.6, -0.05, 'armor')

    @property
    def name(self):
        return self.value[0]

    @property
    def val(self):
        return self.value[1]

    @property
    def upgrade(self):
        return self.value[2]

    @property
    def kind(self):
        return self.value[3]

    @staticmethod
    def getValue(item, level):
        item = Level.getItemByName(item.name)
        if item is None:
            return None
        return item.val + level * item.upgrade

    @staticmethod
    def getItemByName(name):
        for item in Level:
            if item.name == name:
                return item
        return None