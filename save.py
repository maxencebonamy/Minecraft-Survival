from data.enum.effects import Effect
from data.enum.mobs import Mob
from game.rules import Rules


class Save:

    _key = ['g', 'r', 't', 'y', 's', 'u', 'v', 'm', 'a', 'x']

    @staticmethod
    def getPath(*args):
        path = 'data/save'
        for arg in args:
            path += f'/{arg}'
        return path

    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            data = file.readline()

        listData = list(data)
        for i in range(len(listData)):
            listData[i] = str(Save._key.index(listData[i]))

        return int(''.join(listData))

    @staticmethod
    def write(path, value):
        listData = list(str(value))

        for i in range(len(listData)):
            listData[i] = Save._key[int(listData[i])]

        data = ''.join(listData)

        with open(path, 'w') as file:
            file.write(data)


Rules.FPS = Save.read(Save.getPath('settings', 'fps'))
Rules.LANG = Save.read(Save.getPath('settings', 'lang'))
Rules.MUSIC = bool(Save.read(Save.getPath('settings', 'music')))
Rules.SOUND = bool(Save.read(Save.getPath('settings', 'sound')))