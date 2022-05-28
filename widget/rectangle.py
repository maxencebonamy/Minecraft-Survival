import math

import pygame

from game.rules import Rules
from widget._widget import Widget


class Rectangle(Widget):

    def __init__(self, window, position, size, color, outline=0):
        super().__init__(window, position, size)
        self.color = color

        w, h = Rules.SCREEN_SIZE
        self.outline = math.ceil(outline * (w + h) / (1980 + 1080))

    def loop(self):
        super().loop()

        if self.outline == 0:
            # pygame.draw.rect(self.window, self.color, self.rect, self.outline)
            surface = pygame.Surface(self.size)
            surface.set_alpha(self.opacity)
            surface.fill(self.color)
            self.window.blit(surface, self.position)

        else:
            x, y = self.position
            w, h = self.size
            l = self.outline
            dl = l // 2

            pygame.draw.line(self.window, self.color, (x - dl + 1, y), (x + w + dl, y), l)  # haut
            pygame.draw.line(self.window, self.color, (x - dl + 1, y + h), (x + w + dl, y + h), l)  # bas

            pygame.draw.line(self.window, self.color, (x, y - dl + 1), (x, y + h + dl), l)  # gauche
            pygame.draw.line(self.window, self.color, (x + w, y - dl + 1), (x + w, y + h + dl), l)  # droite