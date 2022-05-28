from data.enum.attributes import ObjectAttribute
from data.enum.colors import Color
from game.rules import Rules
from i18n.i18n import i18n
from save import Save
from screen._screen import Screen
from util.anchor import Anchor
from widget.button import Button
from widget.collection.attribute import Attribute
from widget.image import Image
from widget.rectangle import Rectangle
from widget.text import Text


class EffectProfileScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        self.name = Rules.NAME_SELECT

        Rules.BG_COLOR = Color.BG_DARK

        if self.name.onSelf:
            target = i18n('target', 'oneself')
        else:
            target = i18n('target', 'enemy')

        if self.name.uses == -1:
            uses = i18n('unlimited')
        else:
            uses = self.name.uses

        level = Save.read(Save.getPath(self.name.kind, self.name.name))

        self.widgets = {
            # 'topBg': Rectangle(self.window, (0, 0), self.cut.getSize(48, 4), Color.BG_DARK),
            # 'bg': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 23), Color.BG_LIGHT),
            'topOutline': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 0), (255, 255, 255), 2),

            'name': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 4), (255, 255, 255), i18n(self.name.kind, self.name.name), 0.8),
            'closeButton': Button(self.window, self.cut.getPos(1, 1), self.cut.getSize(8, 2), '<<<').setAnimSelect(),

            'imageBg': Rectangle(self.window, self.cut.getPos(26, 5), self.cut.getSize(21, 21), Color.RARITY[self.name.rarity]),
            'image': Image(self.window, self.cut.getPos(29, 8), self.cut.getSize(15, 15), self.name.image),
            'imageOutline': Rectangle(self.window, self.cut.getPos(26, 5), self.cut.getSize(21, 21), (255, 255, 255), 2),

            'rarity': Attribute(self.window, self.cut.getPos(1, 5), self.cut.getSize(24, 2), ObjectAttribute.RARITY, i18n('rarities', self.name.rarity)),
            'level': Attribute(self.window, self.cut.getPos(1, 8), self.cut.getSize(24, 2), ObjectAttribute.LEVEL, level),
            'onSelf': Attribute(self.window, self.cut.getPos(1, 11), self.cut.getSize(24, 2), ObjectAttribute.TARGET, target),
            'uses': Attribute(self.window, self.cut.getPos(1, 14), self.cut.getSize(24, 2), ObjectAttribute.USES, uses, plus=level),
            'duration': Attribute(self.window, self.cut.getPos(1, 17), self.cut.getSize(24, 2), ObjectAttribute.DURATION, self.name.duration),

            'leftOutline': Rectangle(self.window, self.cut.getPos(1, 21), self.cut.getSize(24, 0), (255, 255, 255), 2),

            'info': Text(self.window, self.cut.getPos(1, 23), self.cut.getSize(24, 2), (255, 255, 255), i18n('info_effects', self.name.name)),
        }

    def loop(self):
        super().loop()

        if self.widgets.get('closeButton') in self.clicWidgets:
            self.nextScreen = 'menu'