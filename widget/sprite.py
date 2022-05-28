import math

import pygame

from assets.sprites.sprites import sprites
from game.rules import Rules
from input.input import Input
from widget._widget import Widget


class Sprite(Widget):

    def __init__(self, window, position, size, name):
        super().__init__(window, position, size)

        self.name = name

        self.image = pygame.image.load(f'assets/sprites/{name}.png')
        w = self.image.get_width() // sprites[name]
        h = self.image.get_height()
        self.images = [self.resize(self.image.subsurface((x*w, 0, w, h))) for x in range(sprites[name])]

        self.step = 0
        self.spriteStep = 0

        self.spriteContinue = True

        self.isSprited = 0

    def loop(self):
        super().loop()
        self.window.blit(self.images[self.step], self.rect)

        self.spriteStep += self.isSprited
        if self.spriteStep >= sprites[self.name]:
            if self.spriteContinue:
                self.spriteStep = 0
            else:
                self.isSprited = 0
                self.spriteStep = sprites[self.name] - 1

        self.step = math.floor(self.spriteStep)

        if pygame.K_F3 in Input.keys:
            pygame.draw.rect(self.window, Rules.RECT_COLOR, self.rect, 1)

    def resize(self, image):
        w = image.get_width()
        h = image.get_height()

        if w/h < self.w/self.h:
            w = w * self.h//h
            h = self.h

        else:
            h = h * self.w//w
            w = self.w

        image = pygame.transform.scale(image, (w, h))

        dx = (self.w - w) // 2
        dy = (self.h - h) // 2

        self.rect = pygame.Rect(self.x + dx, self.y + dy, w, h)

        return image

    def setPosition(self, position):
        super().setPosition(position)
        self.images[self.step] = self.resize(self.images[self.step])

    def setSprited(self, speed):
        self.isSprited = speed
        return self

    def setStep(self, step):
        self.step = step
        self.spriteStep = step
        return self