import pygame

from input.input import Input
from screen._screen import Screen


class NameScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        self.widgets = {
            'widgetName': None  # widget
        }

    def loop(self):
        super().loop()

        if Input.clic:
            pass
            # right clic