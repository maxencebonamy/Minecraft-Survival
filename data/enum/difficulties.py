from enum import Enum


class Difficulty(Enum):

    # NAME = ('name', maxStep, rounds, emerald, trophies)

    PEACEFUL = ('peaceful', 30, 10, 20, 5)
    EASY = ('easy', 40, 15, 50, 15)
    NORMAL = ('normal', 50, 20, 100, 25)
    HARDCORE = ('hardcore', 60, 25, 160, 40)

    @property
    def name(self):
        return self.value[0]

    @property
    def maxStep(self):
        return self.value[1]

    @property
    def rounds(self):
        return self.value[2]

    @property
    def emerald(self):
        return self.value[3]

    @property
    def trophies(self):
        return self.value[4]

    @staticmethod
    def increase(difficulty):
        l = [difficulty for difficulty in Difficulty]
        if difficulty == l[-1]:
            return l[0]
        return l[l.index(difficulty) + 1]

    @staticmethod
    def decrease(difficulty):
        l = [difficulty for difficulty in Difficulty]
        if difficulty == l[0]:
            return l[-1]
        return l[l.index(difficulty) - 1]