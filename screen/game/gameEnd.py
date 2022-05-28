from animation.flash import FlashAnimation
from data.enum.colors import Color
from game.rules import Rules
from i18n.i18n import i18n
from images import Import
from output.sound import Sound
from save import Save
from screen._screen import Screen
from widget.button import Button
from widget.menu.property import Property
from widget.text import Text


class GameEndScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.GAME.screen = 'gameEnd'
        Rules.BG_COLOR = Color.BG_DARK

        if Rules.GAME.victory:
            Sound.playSound(Sound.END)
            trophy = Rules.GAME.difficulty.trophies
            emerald = Rules.GAME.difficulty.emerald
            path = Save.getPath('emerald')
            Save.write(path, Save.read(path) + emerald)
        else:
            emerald = 0
            trophy = - Rules.GAME.difficulty.trophies

        for obj in Rules.GAME_MOB, Rules.GAME_EFFECT:
            path = Save.getPath('trophies', obj.name)
            value = Save.read(path) + trophy
            if value < 0:
                value = 0
            if value > 1000:
                value = 1000
            Save.write(path, value)

        text = i18n('victory') if Rules.GAME.victory else i18n('defeat')

        self.widgets = {
            'menuButton': Button(self.window, self.cut.getPos(16, 20), self.cut.getSize(16, 4), i18n('menu')).setAnimSelect(),
            'shadowText': Text(self.window, self.cut.getPos(9.3, 2.3), self.cut.getSize(30, 6), Color.BLACK, text),
            'text': Text(self.window, self.cut.getPos(9, 2), self.cut.getSize(30, 6), Color.RARITY[2], text),
            'emerald': Property(self.window, self.cut.getPos(16, 11), self.cut.getSize(16, 2), str(emerald), Import.EMERALD),
            'trophy': Property(self.window, self.cut.getPos(16, 15), self.cut.getSize(16, 2), str(trophy), Import.TROPHY).setAnimSelect()
        }

        if Rules.GAME.victory:
            self.widgets['text'].animations.append(FlashAnimation(self.widgets['text'], 0.2, Color.RARITY[0]))

    def loop(self):
        super().loop()

        if self.widgets['menuButton'] in self.clicWidgets:
            self.nextScreen = 'menu'