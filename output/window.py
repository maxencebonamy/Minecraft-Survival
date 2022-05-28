import pygame

from data.enum.colors import Color
from game.rules import Rules
from input.input import Input
from screen import screenManager


class Window:

    """
    Fenêtre du jeu
    """

    def __init__(self):

        self.icon = pygame.image.load(Rules.SCREEN_ICON)
        self.icon.set_colorkey((0, 0, 0))

        Rules.SCREEN_SIZE = pygame.display.Info().current_w, pygame.display.Info().current_h

        self.canResize = True
        self.setWindow()

        self.size = self.w, self.h = Rules.SCREEN_SIZE

        self.screens = screenManager.screens

        self.screen = self.screens['menu'](self.window)

    def loop(self):
        if self.screen.nextScreen:
            nextScreen = self.screens[self.screen.nextScreen]
            if self.screen.nextScreen in ('settings', 'menu'):
                self.canResize = True
                self.setWindow()
            elif self.canResize:
                self.canResize = False
                self.setWindow()
            del self.screen
            self.screen = nextScreen(self.window)

        if Input.resize:
            self.setWindow()
            self.screen.__init__(self.window)

        self.window.fill(Rules.BG_COLOR)

        self.screen.loop()

        pygame.display.update()

    def setWindow(self):
        arg = pygame.RESIZABLE if self.canResize else 0
        self.window = pygame.display.set_mode(Rules.SCREEN_SIZE, pygame.FULLSCREEN | pygame.SCALED)
        pygame.display.set_caption(Rules.WINDOW_TITLE)
        pygame.display.set_icon(self.icon)