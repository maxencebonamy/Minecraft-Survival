from animation._animation import Animation
from animation.gradient import GradientAnimation


class FlashAnimation(Animation):

    def __init__(self, widget, time, color):
        super().__init__(widget, time)

        self.color1 = widget.color
        self.color2 = color

        self.gradient = GradientAnimation(widget, time, self.color2)

    def loop(self):
        self.gradient.loop()

        if self.gradient.hasFinished:
            if self.widget.color == self.color2:
                self.gradient.setFinalColor(self.color1)
            elif self.widget.color == self.color1:
                self.gradient.setFinalColor(self.color2)

            self.gradient.hasFinished = False