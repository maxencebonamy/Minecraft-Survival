import math

import pygame

from game.rules import Rules


class ScreenCutting:

    def __init__(self, columns, rows):
        w, h = Rules.SCREEN_SIZE

        self.columns, self.rows = columns, rows

        self.x = w / columns
        self.y = h / rows

    def getPos(self, column, row):
        return round(self.x * column), round(self.y * row)

    def getSize(self, column, row):
        return math.ceil(self.x * column), math.ceil(self.y * row)

    def getOriginPos(self, column, row):
        return round(column / self.x), round(row / self.y)

    def displayCutting(self, window):
        color = Rules.GRID_COLOR

        for i in range(self.columns + 1):
            for j in range(self.rows + 1):
                pygame.draw.rect(window, color, (
                    round(i*self.x),
                    round(j*self.y),
                    round(self.x),
                    round(self.y)
                ), 1)