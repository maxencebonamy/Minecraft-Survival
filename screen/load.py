import pygame

from animation.jump import JumpAnimation
from animation.linear import LinearAnimation
from data.enum.keys import keys
from game.rules import Rules
from images import Import
from input.input import Input
from screen._screen import Screen
from util.screenCutting import ScreenCutting
from widget.image import Image
from widget.polygon import Polygon
from widget.rectangle import Rectangle


class LoadScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        self.cut = ScreenCutting(32, 18)

        self.widgets = {
            'background': Rectangle(self.window, (0, 0), Rules.SCREEN_SIZE, (255, 255, 255)),
            'left': Polygon(self.window, (0, 143, 70), [
                self.cut.getPos(0, 0),
                self.cut.getPos(0, 18),
                self.cut.getPos(14, 18),
                self.cut.getPos(18, 0)
            ]),
            'right': Polygon(self.window, (0, 143, 70), [
                self.cut.getPos(18, 0),
                self.cut.getPos(32, 0),
                self.cut.getPos(32, 18),
                self.cut.getPos(14, 18)
            ]),
            'logo': Image(self.window, self.cut.getPos(6, -10), self.cut.getSize(20, 10), Import.LOGO),
        }

        self.start()

    def loop(self):
        super().loop()

        if not self.isStarting and not self.isEnding:
            if Input.clic:
                self.end()

        if keys['grid'] in Input.keys:
            self.cut.displayCutting(self.window)

    def start(self):
        super(LoadScreen, self).start()

        self.widgets['logo'].animations.append(
            LinearAnimation(self.widgets['logo'], 0.3, self.cut.getPos(6, 4), 0.995)
        )

    def startLoop(self):
        super(LoadScreen, self).startLoop()

        if not self.isAnimated():
            self.widgets['logo'].animations.append(
                JumpAnimation(self.widgets['logo'], 0.5, 10)
            )
            self.isStarting = False

    def end(self):
        super(LoadScreen, self).end()

        self.widgets['logo'].animations.clear()

        self.widgets['logo'].animations.append(
            LinearAnimation(self.widgets['logo'], 0.2, self.cut.getPos(6, -10), 1.1)
        )

        self.widgets['left'].animations.append(
            LinearAnimation(self.widgets['left'], 0.6, self.cut.getPos(-8, 0), 0.999)
        )

        self.widgets['right'].animations.append(
            LinearAnimation(self.widgets['right'], 0.6, self.cut.getPos(22, 0), 0.999)
        )

    def endLoop(self):
        super(LoadScreen, self).endLoop()

        if not self.widgets['left'].animations and not self.widgets['right'].animations:
            self.nextScreen = 'menu'
            del self