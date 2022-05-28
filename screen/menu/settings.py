import pygame

from data.enum.colors import Color
from data.enum.effects import Effect
from data.enum.mobs import Mob
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from output.sound import Sound
from save import Save
from screen._screen import Screen
from util.anchor import Anchor
from widget.button import Button
from widget.rectangle import Rectangle
from widget.text import Text


class SettingsScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.BG_COLOR = Color.BG_DARK

        self.widgets = {
            'topOutline': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), (255, 255, 255), 2),

            'title': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n('settings'), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),
        }

        opts = {
            ('fps', Rules.FPS): (('60', 60), ('120', 120)),
            ('lang', Rules.LANG): (('english', 0), ('francais', 1)),
            ('music', Rules.MUSIC): ((i18n('yes'), True), (i18n('no'), False)),
            ('sound', Rules.SOUND): ((i18n('yes'), True), (i18n('no'), False))
        }

        self.final = {}
        y = 8
        for name, op in opts.items():
            txt, rl = name
            op1, op2 = op
            op1_txt, op1_val = op1
            op2_txt, op2_val = op2
            self.widgets[f'{txt}_txt'] = Text(window, self.cut.getPos(4, y), self.cut.getSize(16, 3), Color.WHITE, i18n(txt), 1, Anchor.LEFT)
            self.widgets[f'{txt}_op1'] = Button(window, self.cut.getPos(22, y), self.cut.getSize(10, 3), op1_txt)
            self.widgets[f'{txt}_op2'] = Button(window, self.cut.getPos(34, y), self.cut.getSize(10, 3), op2_txt)
            if rl == op1_val:
                self.final[txt] = op2_val
                self.widgets[f'{txt}_op2'].setAnimSelect()
                self.widgets[f'{txt}_hid'] = Rectangle(window, self.cut.getPos(34, y-0.5), self.cut.getSize(10, 4), Rules.BG_COLOR).setOpacity(150)
            elif rl == op2_val:
                self.final[txt] = op1_val
                self.widgets[f'{txt}_op1'].setAnimSelect()
                self.widgets[f'{txt}_hid'] = Rectangle(window, self.cut.getPos(22, y-0.5), self.cut.getSize(10, 4), Rules.BG_COLOR).setOpacity(150)
            y += 4

    def loop(self):
        super().loop()

        if self.widgets.get('closeButton') in self.clicWidgets:
            self.nextScreen = 'menu'
        for name, widget in self.widgets.items():
            if 'op' in name and Input.clic and widget.isSelected() and widget.playAnimWhenSelect:
                if 'fps' in name:
                    Rules.FPS = self.final['fps']
                    Save.write(Save.getPath('settings', 'fps'), self.final['fps'])
                elif 'lang' in name:
                    Rules.LANG = self.final['lang']
                    Save.write(Save.getPath('settings', 'lang'), self.final['lang'])
                elif 'music' in name:
                    Rules.MUSIC = self.final['music']
                    Save.write(Save.getPath('settings', 'music'), int(self.final['music']))
                elif 'sound' in name:
                    Rules.SOUND = self.final['sound']
                    Save.write(Save.getPath('settings', 'sound'), int(self.final['sound']))
                    if Rules.SOUND:
                        Sound.playSound(Sound.BUTTON)
                self.__init__(self.window)

        if self.widgets.get('closeButton').isSelected() and pygame.K_h in Input.keys:

            # levels
            if pygame.K_l in Input.keys:
                if pygame.K_UP in Input.keys:
                    for obj in list(Mob) + list(Effect):
                        Save.write(Save.getPath(obj.kind, obj.name), 10)
                elif pygame.K_DOWN in Input.keys:
                    for obj in list(Mob) + list(Effect):
                        Save.write(Save.getPath(obj.kind, obj.name), 0)
                    Rules.GAME_MOB = None
                    Rules.GAME_EFFECT = None

            # trophies
            if pygame.K_t in Input.keys:
                if pygame.K_UP in Input.keys:
                    for obj in list(Mob) + list(Effect):
                        Save.write(Save.getPath('trophies', obj.name), 1000)
                elif pygame.K_DOWN in Input.keys:
                    for obj in list(Mob) + list(Effect):
                        Save.write(Save.getPath('trophies', obj.name), 0)
                    for i in range(1, 37):
                        Save.write(Save.getPath('rewards', str(i)), 0)

            # emerald
            if pygame.K_e in Input.keys:
                if pygame.K_UP in Input.keys:
                    Save.write(Save.getPath('emerald'), 10000)
                elif pygame.K_DOWN in Input.keys:
                    Save.write(Save.getPath('emerald'), 0)