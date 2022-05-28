from screen.game.gameChoice import GameChoiceScreen
from screen.game.gameCollect import GameCollectScreen
from screen.game.gameEnd import GameEndScreen
from screen.game.gameFight import GameFightScreen
from screen.menu.chest import ChestScreen
from screen.menu.effectProfile import EffectProfileScreen
from screen.load import LoadScreen
from screen.menu.menu import MenuScreen
from screen.menu.mobProfile import MobProfileScreen
from screen.menu.objectChoice import ObjectChoiceScreen
from screen.menu.openChest import OpenChestScreen
from screen.menu.play import PlayScreen
from screen.menu.settings import SettingsScreen
from screen.menu.trophies import TrophiesScreen

screens = {
    'load': LoadScreen,
    'menu': MenuScreen,
    'settings': SettingsScreen,
    'trophies': TrophiesScreen,
    'mobProfile': MobProfileScreen,
    'effectProfile': EffectProfileScreen,
    'chest': ChestScreen,
    'openChest': OpenChestScreen,
    'play': PlayScreen,
    'objectChoice': ObjectChoiceScreen,
    'gameCollect': GameCollectScreen,
    'gameChoice': GameChoiceScreen,
    'gameFight': GameFightScreen,
    'gameEnd': GameEndScreen
}