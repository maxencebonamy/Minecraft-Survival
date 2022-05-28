from typing import Tuple

import pygame

from animation.linear import LinearAnimation
from game.rules import Rules
from input.input import Input
from util.screenCutting import ScreenCutting


class Widget:

    def __init__(self, window, position, size):
        self.window = window
        self.position = self.x, self.y = position
        self.size = self.w, self.h = size
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.animations = []
        self.selected = False
        self.prePos = self.position
        self.opacity = 255

        self.playAnimWhenSelect = False

    def loop(self):
        for animation in self.animations:
            animation.loop()
            if animation.hasFinished:
                self.animations.remove(animation)

        if self.playAnimWhenSelect:
            if self.in_instant():
                self.selected = True
                self.animations.clear()
                self.addAnimation(LinearAnimation, 0.1, (self.x, self.y - Rules.SCREEN_SIZE[1] // 130), 1.05)

            elif self.out_instant():
                self.selected = False
                self.animations.clear()
                self.addAnimation(LinearAnimation, 0.1, self.prePos, 1.05)

    def setPosition(self, position):
        self.position = self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def isSelected(self):
        x, y = Input.mouse
        return pygame.Rect(self.prePos[0], self.prePos[1], self.w, self.h).collidepoint(x, y)

    def in_instant(self):
        return self.isSelected() and not self.selected

    def out_instant(self):
        return self.selected and not self.isSelected()

    def setAnimSelect(self, value=True):
        self.playAnimWhenSelect = value
        return self

    def setOpacity(self, opacity):
        self.opacity = opacity
        return self

    def addAnimation(self, animation, *args):
        self.animations.append(animation(self, *args))