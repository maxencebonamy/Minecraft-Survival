import pygame

from animation.linear import LinearAnimation
from data.enum.colors import Color
from data.enum.level import Level
from game.rules import Rules
from i18n.i18n import i18n
from data.enum.items import Item
from input.input import Input
from screen._screen import Screen
from data.enum.tables import Table
from widget.bar import Bar
from widget.button import Button
from widget.image import Image
from widget.menu.selector import Selector
from widget.play.anvil import AnvilWidget
from widget.play.craft import CraftingWidget
from widget.play.enchant import EnchantingWidget
from widget.play.inventory import InventoryWidget
from widget.rectangle import Rectangle
from widget.text import Text


class GameCollectScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.GAME.screen = 'gameCollect'

        Rules.BG_COLOR = Color.BG_DARK

        if Rules.GAME.step == Rules.GAME.maxStep:
            text = i18n('fight')
        else:
            text = '>>>'

        self.widgets = {
            # 'topBg': Rectangle(self.window, (0, 0), self.cut.getSize(48, 4), Color.BG_DARK),
            # 'bottomBg': Rectangle(self.window, self.cut.getPos(0, 23), self.cut.getSize(48, 4), Color.BG_DARK),
            # 'tableBg': Rectangle(self.window, self.cut.getPos(0, 4), self.cut.getSize(48, 3), Color.FG_DARK),
            # 'bg': Rectangle(self.window, self.cut.getPos(0, 7), self.cut.getSize(48, 16), Color.BG_LIGHT),

            'tableTitle': Text(self.window, self.cut.getPos(10, 0), self.cut.getSize(28, 3), Color.WHITE, i18n('tables', Rules.GAME.table.name), 0.7),

            'inventory': Image(self.window, self.cut.getPos(0.25, 5.25), self.cut.getSize(3.5, 3.5), Table.INVENTORY.image),
            'crafting_table': Image(self.window, self.cut.getPos(0.25, 9.25), self.cut.getSize(3.5, 3.5), Table.CRAFTING_TABLE.image),
            'enchanting_table': Image(self.window, self.cut.getPos(0.25, 13.25), self.cut.getSize(3.5, 3.5), Table.ENCHANTING_TABLE.image),
            'anvil': Image(self.window, self.cut.getPos(0.25, 17.25), self.cut.getSize(3.5, 3.5), Table.ANVIL.image),

            'topLine': Rectangle(self.window, self.cut.getPos(0, 3), self.cut.getSize(48, 0), (255, 255, 255), 2),
            'bottomLine': Rectangle(self.window, self.cut.getPos(0, 23), self.cut.getSize(48, 0), (255, 255, 255), 2),
            'tableLine': Rectangle(self.window, self.cut.getPos(4, 3), self.cut.getSize(0, 20), (255, 255, 255), 2),

            'text': Text(self.window, self.cut.getPos(1, 24), self.cut.getSize(8, 2), (255, 255, 255), f'{Rules.GAME.step}/{Rules.GAME.maxStep}', 0.8),
            'textOutline': Rectangle(self.window, self.cut.getPos(1, 24), self.cut.getSize(8, 2), (255, 255, 255), 2),
            'bar': Bar(self.window, self.cut.getPos(10, 24), self.cut.getSize(28, 2), Rules.GAME.step/Rules.GAME.maxStep),
            'nextButton': Button(self.window, self.cut.getPos(39, 24), self.cut.getSize(8, 2), text).setAnimSelect(),
        }

        self.tableWidgets = {
            Table.INVENTORY: InventoryWidget,
            Table.CRAFTING_TABLE: CraftingWidget,
            Table.ENCHANTING_TABLE: EnchantingWidget,
            Table.ANVIL: AnvilWidget
        }

        for table, widget in self.tableWidgets.items():
            if Rules.GAME.table == table:
                self.widgets['displayTable'] = widget(self.window, self.cut.getPos(5, 7), self.cut.getSize(42, 12))
                a, b = self.widgets[table.name].prePos, self.cut.getSize(0.25, 0.25)
                pos = a[0] - b[0], a[1] - b[1]
                self.widgets['selector'] = Selector(self.window, pos, self.cut.getSize(4, 4), Color.WHITE)

    def loop(self):
        super().loop()

        for table in Table:
            if self.widgets[table.name] in self.clicWidgets and self.widgets[table.name].playAnimWhenSelect and not self.widgets['selector'].animations:
                self.widgets['tableTitle'].setText(i18n('tables', table.name))
                self.widgets['displayTable'] = self.tableWidgets[table](self.window, self.cut.getPos(5, 7), self.cut.getSize(42, 12))
                Rules.GAME.table = table
                a, b = self.widgets[table.name].prePos, self.cut.getSize(0.25, 0.25)
                pos = a[0] - b[0], a[1] - b[1]
                self.widgets['selector'].animations.append(
                    LinearAnimation(self.widgets['selector'], 0.2, pos)
                )
            if (table == Table.INVENTORY or Rules.GAME.inventory[Item.getItemByName(table.name)] > 0) \
                    and not self.widgets[table.name].playAnimWhenSelect:
                self.widgets[table.name].setAnimSelect()

        if self.widgets['nextButton'] in self.clicWidgets:
            if Rules.GAME.step < Rules.GAME.maxStep:
                self.nextScreen = 'gameChoice'
            else:
                self.setHotBar()  # todo: remettre
                self.nextScreen = 'gameFight'

        # todo: enlever en dessous
        # if pygame.K_RETURN in Input.keys:
        #     self.setHotBar()
        #     self.nextScreen = 'gameFight'

    def setHotBar(self):
        inv = Rules.GAME.inventory
        lev = Rules.GAME.levels
        kinds = Rules.GAME.hotBar.keys()

        for kind in kinds:
            than = -1 if not kind == 'sword' else 1
            self.setItemHotBar(kind, than)

    def setItemHotBar(self, kind, than=1):
        # than = 1 to >
        inv = Rules.GAME.inventory
        lev = Rules.GAME.levels
        hotBar = Rules.GAME.hotBar

        for item, count in inv.items():
            if kind in item.name and count > 0:
                if not item.enchantable and hotBar[kind][0] is None:
                    Rules.GAME.hotBar[kind] = (item, count, 0)
                elif item.enchantable and (hotBar[kind][0] is None or than*Level.getValue(item, lev[item]) > than*Level.getValue(hotBar[kind][0], hotBar[kind][2])):
                    Rules.GAME.hotBar[kind] = (item, 1, lev[item])