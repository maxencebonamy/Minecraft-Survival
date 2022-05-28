from data.enum.keys import keys, Key
from game.rules import Rules
from input.input import Input
from util.screenCutting import ScreenCutting


class Screen:

    def __init__(self, window):
        self.window = window

        self.cut = ScreenCutting(48, 27)

        self.lang = Rules.LANG

        self.interact = False

        self.widgets = {}

        self.nextScreen = None

        self.clicWidgets = []

    def loop(self):
        self.clicWidgets.clear()

        for widget in self.widgets.values():
            widget.loop()
            if Input.clic and widget.isSelected():
                self.clicWidgets.append(widget)

        if Key.GRID in Input.keys:
            self.cut.displayCutting(self.window)

    def isAnimated(self):
        for widget in self.widgets.values():
            if widget.animations:
                return True
        return False