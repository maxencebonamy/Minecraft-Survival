import random

from data.enum.colors import Color
from data.enum.items import Item
from data.enum.tables import Table
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from widget._widget import Widget
from widget.button import Button
from widget.play.item import ItemWidget
from widget.rectangle import Rectangle
from widget.text import Text


class CraftingWidget(Widget):

    def __init__(self, window, position, size):
        super().__init__(window, position, size)

        # size = (42, 12)

        self.widgets = {}

        self.resetItems()

        item = random.choice(list(Item))
        while item.natural or item == Item.EMPTY:
            item = random.choice(list(Item))
        self.setCraft(item)

        self.newTable = None

    def loop(self):
        super().loop()

        itemSelected = None
        for name, widget in self.widgets.items():
            widget.loop()

            if Input.clic and 'item' in name and widget.isSelected():
                itemSelected = Item.getItemByName(name[4:])

        if itemSelected:
            self.setCraft(itemSelected)

        if Input.clic and self.widgets.get('buttonCraft'):
            if self.widgets['buttonCraft'].playAnimWhenSelect and self.widgets['buttonCraft'].isSelected():
                for mat, nb in self.materials.items():
                    Rules.GAME.inventory[mat] -= nb
                mat, nb = self.item
                Rules.GAME.inventory[mat] += nb
                self.setCraft(mat)
                self.resetItems()
                if mat in (Item.ENCHANTING_TABLE, Item.ANVIL):
                    self.newTable = Table.getTableByName(mat.name)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 42 * x), round(self.position[1] + self.size[1] / 12 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 42 * w), round(self.size[1] / 12 * h)

    def setCraft(self, item):
        toDelete = [name for name in self.widgets.keys() if name[:5] == 'craft']
        for name in toDelete:
            del self.widgets[name]

        coords = [
            [(31, 2), (36, 2), (28, 2)],
            [(32.5, 2), (37, 2), (27, 2), (30, 2)],
            [(34, 2), (38, 2), (26, 2), (29, 2), (32, 2)],
        ]

        result = 1
        self.materials = {}
        for material, nb in item.craft:
            if material == 'result':
                result = nb
            else:
                self.materials[Item.getItemByName(material[0])] = nb

        coords = coords[len(self.materials) - 1]

        self.item = (item, result)

        for index, material in enumerate(self.materials.items()):
            mat, nb = material
            self.widgets[f'craft{mat.name}'] = ItemWidget(self.window, self.getPos(*coords[index+2]), self.getSize(3, 3), mat, nb)

        self.widgets['arrow'] = Text(self.window, self.getPos(*coords[0]), self.getSize(5, 3), Color.WHITE, '>>>', 0.5)

        self.widgets['finalItem'] = ItemWidget(self.window, self.getPos(*coords[1]), self.getSize(3, 3), item, result)

        self.widgets['buttonCraft'] = Button(self.window, self.getPos(27, 7), self.getSize(13, 3), i18n('craft'))
        if self.canCraft(item):
            self.widgets['buttonCraft'].setAnimSelect()

    def canCraft(self, item):
        if Rules.GAME.inventory[item] == 1 and item.enchantable:
            return False
        for it, nb in item.craft:
            it = Item.getItemByName(it[0])
            if it is not None and Rules.GAME.inventory[it] < nb:
                return False
        return True

    def resetItems(self):
        coords = [(x * 3, y * 3) for x in range(8) for y in range(4)]
        items = [item for item in Item if not item.natural]
        for key, value in enumerate(items):
            if value != Item.EMPTY:
                nb = None if self.canCraft(value) else 0
                self.widgets[f'item{value.name}'] = ItemWidget(self.window, self.getPos(*coords[key]), self.getSize(3, 3), value, nb).setAnimSelect()

        self.widgets['outline'] = Rectangle(self.window, self.getPos(25, 0), self.getSize(17, 12), Color.WHITE, 2)