import pygame

from widget._widget import Widget


class Ellipse(Widget):

    def __init__(self, window, position, size, color, outline=0):
        super().__init__(window, position, size)
        self.color = color
        self.outline = outline

    def loop(self):
        super().loop()

        pygame.draw.ellipse(self.window, self.color, self.rect, self.outline)