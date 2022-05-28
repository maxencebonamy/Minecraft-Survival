from animation._animation import Animation
from widget.image import Image


class ResizeAnimation(Animation):

    def __init__(self, widget, time, finalSize):
        super().__init__(widget, time)

        self.finalSize = self.fw, self.fh = finalSize
        self.size = self.w, self.h = widget.size

        self.dw = (self.fw - self.w) / self.time
        self.dh = (self.fh - self.h) / self.time

    def loop(self):
        self.calcSize()
        self.widget.setSize(self.size)

    def calcSize(self):
        if self.w != self.fw:
            self.w += self.dw
            if abs(self.w - self.fw) < abs(self.dw):
                self.w = self.fw

        if self.h != self.fh:
            self.h += self.dh
            if abs(self.h - self.fh) < abs(self.dh):
                self.h = self.fh

        self.size = round(self.w), round(self.h)

        if self.w == self.fw and self.h == self.fh:
            self.hasFinished = True