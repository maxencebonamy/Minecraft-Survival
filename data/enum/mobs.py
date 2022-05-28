import random
from enum import Enum

from data.enum.effects import Effect
from images import Import


class Mob(Enum):

    # NAME = (name, rarity, health, damage, distance, effects, image, world)

    SILVER_FISH = ('silver_fish', 1, 4, 1, 0, {}, Import.MOB.SILVER_FISH, 'overworld')
    SPIDER = ('spider', 1, 8, 2, 0, {}, Import.MOB.SPIDER, 'overworld')
    SKELETON = ('skeleton', 1, 10, 3, 2, {}, Import.MOB.SKELETON, 'overworld')
    SLIME = ('slime', 1, 8, 2, 0, {}, Import.MOB.SLIME, 'overworld')
    ZOMBIE = ('zombie', 1, 10, 3, 0, {}, Import.MOB.ZOMBIE, 'overworld')
    ENDERMITE = ('endermite', 1, 4, 1, 0, {}, Import.MOB.ENDERMITE, 'end')

    CREEPER = ('creeper', 2, 10, 0, 0, {Effect.BLOW_UP: 1}, Import.MOB.CREEPER, 'overworld')
    WITCH = ('witch', 2, 13, 0, 1, {Effect.POISON: 4, Effect.FIRE_RESISTANCE: -1}, Import.MOB.WITCH, 'overworld')
    CAVE_SPIDER = ('cave_spider', 2, 6, 2, 0, {Effect.POISON: 2}, Import.MOB.CAVE_SPIDER, 'overworld')
    PIGMAN = ('pigman', 2, 10, 3, 0, {Effect.FIRE_RESISTANCE: -1}, Import.MOB.PIGMAN, 'nether')
    BLAZE = ('blaze', 2, 10, 3, 2, {Effect.FIRE: 2, Effect.FIRE_RESISTANCE: -1}, Import.MOB.BLAZE, 'nether')
    MAGMA_CUBE = ('magma_cube', 2, 8, 2, 0, {Effect.FIRE_RESISTANCE: -1}, Import.MOB.MAGMA_CUBE, 'nether')

    GUARDIAN = ('guardian', 3, 15, 4, 1, {Effect.FIRE_RESISTANCE: -1}, Import.MOB.GUARDIAN, 'overworld')
    GHAST = ('ghast', 3, 10, 4, 3, {Effect.FIRE: 3, Effect.FIRE_RESISTANCE: -1}, Import.MOB.GHAST, 'nether')
    WITHER_SKELETON = ('wither_skeleton', 3, 20, 4, 0, {Effect.POISON: 3}, Import.MOB.WITHER_SKELETON, 'nether')
    ENDERMAN = ('enderman', 3, 20, 4, 0, {}, Import.MOB.ENDERMAN, 'end')

    ELDER_GUARDIAN = ('elder_guardian', 4, 30, 6, 9, {Effect.FIRE_RESISTANCE: -1}, Import.MOB.ELDER_GUARDIAN, 'overworld')
    WITHER = ('wither', 4, 30, 6, 9, {Effect.POISON: 5, Effect.FIRE: 3}, Import.MOB.WITHER, 'nether')
    ENDER_DRAGON = ('ender_dragon', 4, 30, 6, 9, {Effect.FIRE: 3, Effect.FIRE_RESISTANCE: -1}, Import.MOB.ENDER_DRAGON, 'end')

    @property
    def name(self):
        return self.value[0]

    @property
    def rarity(self):
        return self.value[1]

    @property
    def health(self):
        return self.value[2]

    @property
    def damage(self):
        return self.value[3]

    @property
    def distance(self):
        return self.value[4]

    @property
    def effects(self):
        return self.value[5]

    @property
    def image(self):
        return self.value[6]

    @property
    def world(self):
        return self.value[7]

    @property
    def kind(self):
        return 'mob'

    @staticmethod
    def get(name):
        for i in Mob:
            if i.name == name:
                return i

    @staticmethod
    def sort(rarity=None):
        if rarity is None:
            return random.choice([mob for mob in Mob])
        return random.choice([mob for mob in Mob if mob.rarity == rarity])

    @staticmethod
    def getKind():
        return 'mob'