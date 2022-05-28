import numpy
import pygame

from game.rules import Rules
from input.input import Input
from widget._widget import Widget


class Image(Widget):

    def __init__(self, window, position, size, image):
        super().__init__(window, position, size)
        self.initialImage = image
        self.image = image
        self.resize()

    def loop(self):
        super().loop()

        self.window.blit(self.image, self.rect)

        if pygame.K_F3 in Input.keys:
            pygame.draw.rect(self.window, Rules.RECT_COLOR, self.rect, 1)

    def resize(self):
        w = self.initialImage.get_width()
        h = self.initialImage.get_height()

        if w/h < self.w/self.h:
            w = w * self.h//h
            h = self.h

        else:
            h = h * self.w//w
            w = self.w

        self.image = pygame.transform.scale(self.initialImage, (w, h))

        dx = (self.w - w) // 2
        dy = (self.h - h) // 2

        self.rect = pygame.Rect(self.x + dx, self.y + dy, w, h)

    def setPosition(self, position):
        super().setPosition(position)
        self.resize()

    def setSize(self, size):
        self.w, self.h = size
        self.resize()

    def toBlackAndWhite(self):
        arr = pygame.surfarray.array3d(self.image)
        # luminosity filter
        avgs = [[(r * 0.298 + g * 0.587 + b * 0.114) for (r, g, b) in col] for col in arr]
        arr = numpy.array([[[avg, avg, avg] for avg in col] for col in avgs])
        self.image = pygame.surfarray.make_surface(arr)