import pygame

from animation._animation import Animation
from animation.linear import LinearAnimation


class JumpAnimation(Animation):

    def __init__(self, widget, time, height, jumps=None):
        super().__init__(widget, time)

        self.height = height

        self.y0 = self.y
        self.y1 = self.y - self.height

        self.linear = LinearAnimation(self.widget, time, (self.x, self.y - height), 1.05)

        self.jumps = 0
        self.maxJumps = jumps

    def loop(self):
        if self.maxJumps is None or self.jumps < self.maxJumps:
            self.linear.loop()

            if self.linear.hasFinished:
                self.jumps += 1
                if self.linear.y == self.y1:
                    self.linear.setFinalPosition((self.x, self.y0))
                else:
                    self.linear.setFinalPosition((self.x, self.y1))

                self.linear.hasFinished = False
        else:
            self.hasFinished = True