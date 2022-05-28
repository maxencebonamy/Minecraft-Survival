import random

from data.enum.effects import Effect
from data.enum.items import Item
from data.enum.mobs import Mob
from data.enum.tables import Table


class Game:

    def __init__(self, difficulty):
        self.screen = 'gameCollect'
        self.table = Table.INVENTORY

        self.difficulty = difficulty

        self.step = 0
        self.maxStep = difficulty.maxStep

        self.effect = None

        self.inventory = {item: 0 for item in Item}
        self.inventory[Item.CRAFTING_TABLE] = 1

        self.levels = {item: 0 for item in Item if item.enchantable}

        self.items = self.setItems()

        self.hotBar = {}

        for key in 'helmet', 'chestplate', 'leggings', 'boots', 'sword', 'bow', 'flint_and_steel', 'arrow', 'golden_apple':
            self.hotBar[key] = (None, None, None)

        # self.hotBar = {'helmet': (Item.HELMET, count, level)}

        self.mobs = self.setMobs()
        self.round = 1

        self.victory = False

    def setItems(self):
        finalItems = []
        for i in range(self.maxStep):
            items = {}
            for k in range(4):
                it = None
                while it is None or it in items or not it.natural:
                    it = random.choice(list(Item))
                nb = random.randint(*it.craft)
                if self.effect == Effect.LUCK:
                    nb += 1
                elif self.effect == Effect.HASTE and it in (Item.DIAMOND, Item.GOLD_INGOT, Item.IRON_INGOT):
                    nb += 3
                items[it] = nb
            finalItems.append(items)
        return finalItems

    def setMobs(self):
        rnds = self.difficulty.rounds
        nt_rnd = round((rnds - 4) / 3)
        ov_rnd = rnds - nt_rnd - 4
        worlds = ['overworld'] * ov_rnd + ['overworld_boss'] + ['nether'] * nt_rnd + ['nether_boss'] + ['end'] + ['end_boss']

        mobs = []
        for world in worlds:
            # boss
            if 'boss' in world:
                mobs.append({5: self.drawMob(world[0:-5], True)})
            # mobs
            else:
                rnd = {}
                for i in range(random.randint(1, 5)):
                    place = None
                    while place is None or place in rnd.keys():
                        place = random.randint(1, 9)
                    rnd[place] = self.drawMob(world)
                mobs.append(rnd)

        return mobs

    def drawMob(self, world, boss=False):
        mobs = [mob for mob in Mob if world == mob.world]
        if boss:
            mobs = [mob for mob in mobs if mob.rarity == 4]
        else:
            mobs = [mob for mob in mobs if mob.rarity != 4]

        return random.choice(mobs)