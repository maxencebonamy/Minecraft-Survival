import pygame

from animation._animation import Animation


class LinearAnimation(Animation):

    def __init__(self, widget, time, finalPosition, acc=1):
        super().__init__(widget, time)
        self.widget = widget

        self.finalPosition = self.fx, self.fy = finalPosition

        self.dx = (self.fx - self.x) / self.time
        self.dy = (self.fy - self.y) / self.time

        self.acc = acc

    def loop(self):
        self.calcPosition()
        self.widget.setPosition(self.position)

    def calcPosition(self):
        self.dx *= self.acc
        self.dy *= self.acc

        if self.x != self.fx:
            self.x = self.x + self.dx
            if abs(self.x - self.fx) < abs(self.dx):
                self.x = self.fx

        if self.y != self.fy:
            self.y = self.y + self.dy
            if abs(self.y - self.fy) < abs(self.dy):
                self.y = self.fy

        self.position = round(self.x), round(self.y)

        if self.x == self.fx and self.y == self.fy:
            self.hasFinished = True

    def setFinalPosition(self, position):
        self.finalPosition = self.fx, self.fy = position

        self.dx = (self.fx - self.x) / self.time
        self.dy = (self.fy - self.y) / self.time