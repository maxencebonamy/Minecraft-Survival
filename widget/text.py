import pygame

from game.rules import Rules
from input.input import Input
from util.anchor import Anchor
from widget._widget import Widget


class Text(Widget):

    def __init__(self, window, position, size, color, string, fill=1, anchor=Anchor.CENTER):
        super().__init__(window, position, size)
        self.color = color
        self.string = string
        self.fill = fill
        self.anchor = anchor

        self.fontPath = Rules.FONT

        self.font = pygame.font.Font(self.fontPath, 1)
        self.text = self.font.render(self.string, True, self.color)

        self.load()
        self.setAnchor(self.anchor)

    def loop(self):
        super().loop()

        self.window.blit(self.text, self.rect)

        if pygame.K_F3 in Input.keys:
            pygame.draw.rect(self.window, Rules.RECT_COLOR, self.rect, 1)

    def load(self):
        size = 1
        while self.text.get_width() < self.w * self.fill and self.text.get_height() < self.h * self.fill:
            size += 1
            self.font = pygame.font.Font(self.fontPath, size)
            self.text = self.font.render(self.string, True, self.color)

    def setAnchor(self, side):
        w = self.text.get_width()
        h = self.text.get_height()
        dx = (self.w - w) // 2
        dy = (self.h - h) // 2

        self.rect = pygame.Rect(self.x + side.x*dx, self.y + side.y*dy, w, h)

        return self

    def setPosition(self, position):
        super().setPosition(position)
        self.setAnchor(self.anchor)

    def setColor(self, color):
        self.color = color
        self.text = self.font.render(self.string, True, self.color)
        self.load()

    def setText(self, text):
        self.string = text
        self.text = self.font.render(self.string, True, self.color)
        self.load()
        self.setAnchor(self.anchor)