from enum import Enum


class Anchor(Enum):

    LEFT = (0, 1)
    RIGHT = (2, 1)
    TOP = (1, 0)
    BOTTOM = (1, 2)

    LEFT_TOP = (0, 0)
    LEFT_BOTTOM = (0, 2)
    RIGHT_TOP = (2, 0)
    RIGHT_BOTTOM = (2, 2)

    CENTER = (1, 1)

    @property
    def x(self):
        return self.value[0]

    @property
    def y(self):
        return self.value[1]