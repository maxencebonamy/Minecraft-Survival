import pygame

from game.rules import Rules
from input.input import Input
from widget._widget import Widget


class Polygon(Widget):

    def __init__(self, window, color, points, outline=0):
        rect = pygame.draw.polygon(window, color, points, outline)

        super().__init__(window, (rect.x, rect.y), (rect.width, rect.height))
        self.color = color
        self.outline = outline
        self.points = points

    def loop(self):
        super().loop()

        pygame.draw.polygon(self.window, self.color, self.points, self.outline)

        if pygame.K_F3 in Input.keys:
            pygame.draw.rect(self.window, Rules.RECT_COLOR, self.rect, 1)

    def setPosition(self, position):
        dx = position[0] - self.x
        dy = position[1] - self.y

        for p in range(len(self.points)):
            point = self.points[p]
            self.points[p] = (point[0] + dx, point[1] + dy)

        super().setPosition(position)