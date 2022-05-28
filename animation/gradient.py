from animation._animation import Animation


class GradientAnimation(Animation):

    def __init__(self, widget, time, finalColor):
        super().__init__(widget, time)

        assert widget.color is not None

        self.fr, self.fg, self.fb = self.finalColor = finalColor
        self.r, self.g, self.b = self.widget.color

        self.variation = (
            (self.fr - self.r) / self.time,
            (self.fg - self.g) / self.time,
            (self.fb - self.b) / self.time
        )

    def loop(self):
        if not self.hasFinished:
            if self.finalColor != self.widget.color:
                r, g, b = self.widget.color
                dr, dg, db = self.variation

                nr, ng, nb = r + dr, g + dg, b + db
                if abs(self.fr - r) < abs(dr):
                    nr = self.fr
                if abs(self.fg - g) < abs(dg):
                    ng = self.fg
                if abs(self.fb - b) < abs(db):
                    nb = self.fb

                self.widget.setColor((round(nr), round(ng), round(nb)))
            else:
                self.hasFinished = True

    def setFinalColor(self, finalColor):
        self.finalColor = finalColor
        self.fr, self.fg, self.fb = finalColor
        self.r, self.g, self.b = self.widget.color

        self.variation = None
        self.variation = (
            (self.fr - self.r) / self.time,
            (self.fg - self.g) / self.time,
            (self.fb - self.b) / self.time
        )