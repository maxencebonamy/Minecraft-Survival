from animation._animation import Animation


class OpacityAnimation(Animation):

    def __init__(self, widget, time, finalOpacity):
        super().__init__(widget, time)

        self.finalOpacity = finalOpacity

        self.variation = (self.finalOpacity - self.widget.opacity) / time

    def loop(self):
        if self.finalOpacity != self.widget.opacity:
            self.widget.opacity = round(self.widget.opacity + self.variation)

            if abs(self.widget.opacity - self.finalOpacity) < abs(self.variation):
                self.widget.opacity = self.finalOpacity
        else:
            self.hasFinished = True