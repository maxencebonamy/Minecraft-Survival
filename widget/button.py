import pygame

from animation.linear import LinearAnimation
from images import Import
from input.input import Input
from output.sound import Sound
from widget.image import Image
from widget.text import Text
from widget._widget import Widget


class Button(Widget):

    def __init__(self, window, position, size, text, prePos=None):
        super().__init__(window, position, size)

        self.image = Image(window, position, size, Import.BUTTON)

        self.text = Text(window, position, size, (255, 255, 255), text, 0.6)

        if prePos:
            self.prePos = prePos

    def loop(self):
        super().loop()

        self.image.loop()
        self.text.loop()

        if Input.clic and self.isSelected():
            Sound.playSound(Sound.BUTTON)

    def setPosition(self, position):
        super().setPosition(position)
        self.image.setPosition(position)
        self.text.setPosition(position)