from enum import Enum

from data.enum.difficulties import Difficulty
from data.enum.effects import Effect
from data.enum.items import Item
from data.enum.mobs import Mob
from save import Save


class Quest(Enum):

    # QUEST = (name, count, reward, objects)

    # tuer 25 monstres (creeper) -> 10 emeraudes
    KILL_MOB = ('kill_mob', (25, 50, 100, 200), (10, 20, 50, 100), tuple(Mob))

    # utiliser 25 effets (nausee) -> 10 emeraudes
    USE_EFFECT = ('use_effect', (25, 50, 100, 200), (10, 20, 50, 100), tuple(Effect))

    # fabriquer 25 objets (bloc de fer) -> 10 emeraudes
    CRAFT_ITEM = ('craft_item', (25, 50, 100, 200), (10, 20, 50, 100), tuple([it for it in Item if it != Item.EMPTY]))

    # gagner 2 parties (difficile) -> 20 emeraudes
    WIN_GAME = ('win_game', (2, 5, 10), (20, 50, 100), tuple(Difficulty))

    # gagner 2 parties (nausee) -> 20 emeraudes
    WIN_GAME_EFFECT = ('win_game_effect', (2, 5, 10), (20, 50, 100),
                       tuple([ef for ef in Effect if Save.read(Save.getPath('effect', ef.name)) > 0]))

    # gagner 2 parties (creeper) -> 20 emeraudes
    WIN_GAME_MOB = ('win_game_mob', (2, 5, 10), (20, 50, 100),
                    tuple([mo for mo in Mob if Save.read(Save.getPath('mob', mo.name)) > 0]))

    # ameliorer 1 objet (niveau 1) -> 5 emeraudes
    UPGRADE_ITEM = ('upgrade_item', (1, 2, 3), (5, 10, 20), tuple([it for it in Item if it.enchantable]))

    @property
    def name(self):
        return self.value[0]

    @property
    def count(self):
        return self.value[1]

    @property
    def reward(self):
        return self.value[2]

    @property
    def objects(self):
        return self.value[3]