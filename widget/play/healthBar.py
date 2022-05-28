from images import Import
from output.sound import Sound
from widget._widget import Widget
from widget.image import Image


class HealthBar(Widget):

    def __init__(self, window, position, size, maxHealth, proportions):
        super().__init__(window, position, size)

        self.maximum = proportions[0] * proportions[1]

        self.proportions = proportions
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.absorption = 0

        self.setHearts()

    def loop(self):
        super().loop()
        for heart in self.hearts:
            heart.loop()

    def setPosition(self, position):
        super().setPosition(position)
        self.setHearts()

    def setAbsorption(self, hearts):
        while hearts > 0:
            if self.absorption + self.maxHealth < self.maximum:
                self.absorption += 1
            hearts -= 1
        self.setHearts()

    def setHearts(self):
        self.hearts = []
        coords = [self.getPos(x, self.proportions[1]-y-1) for y in range(self.proportions[1]) for x in range(self.proportions[0])]
        i = 0
        while i < self.health:
            self.hearts.append(Image(self.window, coords[i], self.getSize(1, 1), Import.HEART))
            i += 1
        while i < self.maxHealth:
            self.hearts.append(Image(self.window, coords[i], self.getSize(1, 1), Import.HEART_EMPTY))
            i += 1
        while i < self.maxHealth + self.absorption:
            self.hearts.append(Image(self.window, coords[i], self.getSize(1, 1), Import.HEART_ABSORPTION))
            i += 1

    def damage(self, hearts=1):
        Sound.playSound(Sound.DAMAGE)
        hearts = round(hearts)
        while hearts > 0:
            if self.absorption > 0:
                self.absorption -= 1
            elif self.health > 0:
                self.health -= 1
            hearts -= 1
        self.setHearts()

    def heal(self, hearts=1):
        Sound.playSound(Sound.ORB)
        if self.health < self.maxHealth:
            self.health += hearts
            self.setHearts()

    def setHealth(self, hearts):
        if 0 <= hearts <= self.maxHealth:
            self.health = hearts
        self.setHearts()
        return self

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / self.proportions[0] * x),\
               round(self.position[1] + self.size[1] / self.proportions[1] * y)

    def getSize(self, w, h):
        return round(self.size[0] / self.proportions[0] * w),\
               round(self.size[1] / self.proportions[1] * h)