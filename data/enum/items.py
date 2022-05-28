from enum import Enum

from data.enum.colors import Color
from images import Import


class Item(Enum):

    # NAME = ('name', craft, image, natural, color, enchantable)

    WOOD_LOG = ('wood_log', (2, 3), Import.ITEM.WOOD_LOG, True, Color.RARITY[1], False)
    OBSIDIAN = ('obsidian', (1, 2), Import.ITEM.OBSIDIAN, True, Color.RARITY[1], False)
    SUGAR_CANE = ('sugar_cane', (3, 6), Import.ITEM.SUGAR_CANE, True, Color.RARITY[1], False)
    APPLE = ('apple', (1, 2), Import.ITEM.APPLE, True, Color.RARITY[1], False)
    DIAMOND = ('diamond', (4, 6), Import.ITEM.DIAMOND, True, Color.RARITY[1], False)
    IRON_INGOT = ('iron_ingot', (6, 8), Import.ITEM.IRON_INGOT, True, Color.RARITY[1], False)
    GOLD_INGOT = ('gold_ingot', (4, 6), Import.ITEM.GOLD_INGOT, True, Color.RARITY[1], False)
    STRING = ('string', (2, 3), Import.ITEM.STRING, True, Color.RARITY[1], False)
    FEATHER = ('feather', (6, 8), Import.ITEM.FEATHER, True, Color.RARITY[1], False)
    FLINT = ('flint', (6, 8), Import.ITEM.FLINT, True, Color.RARITY[1], False)
    LEATHER = ('leather', (1, 3), Import.ITEM.LEATHER, True, Color.RARITY[1], False)
    EXPERIENCE_BOTTLE = ('experience_bottle', (1, 2), Import.ITEM.EXPERIENCE_BOTTLE, True, Color.RARITY[1], False)

    WOOD_PLANKS = ('wood_planks', ((WOOD_LOG, 1), ('result', 4)), Import.ITEM.WOOD_PLANKS, False, Color.RARITY[1], False)
    STICK = ('stick', ((WOOD_PLANKS, 2), ('result', 4)), Import.ITEM.STICK, False, Color.RARITY[1], False)
    IRON_BLOCK = ('iron_block', ((IRON_INGOT, 9),), Import.ITEM.IRON_BLOCK, False, Color.RARITY[1], False)
    CRAFTING_TABLE = ('crafting_table', ((WOOD_PLANKS, 4),), Import.ITEM.CRAFTING_TABLE, False, Color.RARITY[1], False)
    PAPER = ('paper', ((SUGAR_CANE, 3), ('result', 3)), Import.ITEM.PAPER, False, Color.RARITY[1], False)
    BOOK = ('book', ((PAPER, 3), (LEATHER, 1)), Import.ITEM.BOOK, False, Color.RARITY[1], False)
    ENCHANTING_TABLE = ('enchanting_table', ((OBSIDIAN, 4), (DIAMOND, 2), (BOOK, 1)), Import.ITEM.ENCHANTING_TABLE, False, Color.RARITY[1], False)
    ANVIL = ('anvil', ((IRON_INGOT, 4), (IRON_BLOCK, 3)), Import.ITEM.ANVIL, False, Color.RARITY[1], False)
    FLINT_AND_STEEL = ('flint_and_steel', ((IRON_INGOT, 1), (FLINT, 1)), Import.ITEM.FLINT_AND_STEEL, False, Color.RARITY[4], True)
    BOW = ('bow', ((STICK, 3), (STRING, 3)), Import.ITEM.BOW, False, Color.RARITY[4], True)
    ARROW = ('arrow', ((FLINT, 1), (STICK, 1), (FEATHER, 1), ('result', 4)), Import.ITEM.ARROW, False, Color.RARITY[2], False)
    GOLDEN_APPLE = ('golden_apple', ((APPLE, 1), (GOLD_INGOT, 8)), Import.ITEM.GOLDEN_APPLE, False, Color.RARITY[2], False)
    WOODEN_SWORD = ('wooden_sword', ((STICK, 1), (WOOD_PLANKS, 2)), Import.ITEM.WOODEN_SWORD, False, Color.RARITY[4], True)
    GOLDEN_SWORD = ('golden_sword', ((STICK, 1), (GOLD_INGOT, 2)), Import.ITEM.GOLDEN_SWORD, False, Color.RARITY[4], True)
    IRON_SWORD = ('iron_sword', ((STICK, 1), (IRON_INGOT, 2)), Import.ITEM.IRON_SWORD, False, Color.RARITY[4], True)
    DIAMOND_SWORD = ('diamond_sword', ((STICK, 1), (DIAMOND, 2)), Import.ITEM.DIAMOND_SWORD, False, Color.RARITY[4], True)

    LEATHER_HELMET = ('leather_helmet', ((LEATHER, 5),), Import.ITEM.LEATHER_HELMET, False, Color.RARITY[3], True)
    LEATHER_CHESTPLATE = ('leather_chestplate', ((LEATHER, 8),), Import.ITEM.LEATHER_CHESTPLATE, False, Color.RARITY[3], True)
    LEATHER_LEGGINGS = ('leather_leggings', ((LEATHER, 7),), Import.ITEM.LEATHER_LEGGINGS, False, Color.RARITY[3], True)
    LEATHER_BOOTS = ('leather_boots', ((LEATHER, 4),), Import.ITEM.LEATHER_BOOTS, False, Color.RARITY[3], True)
    GOLDEN_HELMET = ('golden_helmet', ((GOLD_INGOT, 5),), Import.ITEM.GOLDEN_HELMET, False, Color.RARITY[3], True)
    GOLDEN_CHESTPLATE = ('golden_chestplate', ((GOLD_INGOT, 8),), Import.ITEM.GOLDEN_CHESTPLATE, False, Color.RARITY[3], True)
    GOLDEN_LEGGINGS = ('golden_leggings', ((GOLD_INGOT, 7),), Import.ITEM.GOLDEN_LEGGINGS, False, Color.RARITY[3], True)
    GOLDEN_BOOTS = ('golden_boots', ((GOLD_INGOT, 4),), Import.ITEM.GOLDEN_BOOTS, False, Color.RARITY[3], True)
    IRON_HELMET = ('iron_helmet', ((IRON_INGOT, 5),), Import.ITEM.IRON_HELMET, False, Color.RARITY[3], True)
    IRON_CHESTPLATE = ('iron_chestplate', ((IRON_INGOT, 8),), Import.ITEM.IRON_CHESTPLATE, False, Color.RARITY[3], True)
    IRON_LEGGINGS = ('iron_leggings', ((IRON_INGOT, 7),), Import.ITEM.IRON_LEGGINGS, False, Color.RARITY[3], True)
    IRON_BOOTS = ('iron_boots', ((IRON_INGOT, 4),), Import.ITEM.IRON_BOOTS, False, Color.RARITY[3], True)
    DIAMOND_HELMET = ('diamond_helmet', ((DIAMOND, 5),), Import.ITEM.DIAMOND_HELMET, False, Color.RARITY[3], True)
    DIAMOND_CHESTPLATE = ('diamond_chestplate', ((DIAMOND, 8),), Import.ITEM.DIAMOND_CHESTPLATE, False, Color.RARITY[3], True)
    DIAMOND_LEGGINGS = ('diamond_leggings', ((DIAMOND, 7),), Import.ITEM.DIAMOND_LEGGINGS, False, Color.RARITY[3], True)
    DIAMOND_BOOTS = ('diamond_boots', ((DIAMOND, 4),), Import.ITEM.DIAMOND_BOOTS, False, Color.RARITY[3], True)

    EMPTY = ('empty', (), Import.EMPTY, False, Color.GRAY, False)

    @property
    def name(self):
        return self.value[0]

    @property
    def craft(self):
        return self.value[1]

    @property
    def image(self):
        return self.value[2]

    @property
    def natural(self):
        return self.value[3]

    @property
    def color(self):
        return self.value[4]

    @property
    def enchantable(self):
        return self.value[5]

    @staticmethod
    def getItemByName(name):
        for item in Item:
            if item.name == name:
                return item
        return None

    @property
    def toTuple(self):
        return self.value