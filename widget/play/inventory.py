import random

from data.enum.colors import Color
from data.enum.items import Item
from data.enum.level import Level
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from widget._widget import Widget
from widget.play.item import ItemWidget
from widget.rectangle import Rectangle
from widget.text import Text


class InventoryWidget(Widget):

    def __init__(self, window, position, size):
        super().__init__(window, position, size)

        # size = (42, 12)

        coords = [(x * 3, y * 3) for x in range(11) for y in range(4)]

        self.widgets = {}

        for nb, item in enumerate(Item):
            if item != Item.EMPTY:
                self.widgets[f'item{item.name}'] = ItemWidget(self.window, self.getPos(*coords[nb]), self.getSize(3, 3), item,
                                                              Rules.GAME.inventory[item], Rules.GAME.levels.get(item)).setAnimSelect() \
                    if Rules.GAME.inventory[item] > 0 else Rectangle(self.window, self.getPos(*coords[nb]), self.getSize(3, 3), Color.WHITE, 2)

        item = None
        while item is None or Rules.GAME.inventory[item] == 0:
            item = random.choice(list(Item))
        self.setItem(item)

    def loop(self):
        super().loop()

        item = None
        for widget in self.widgets.values():
            widget.loop()

            if Input.clic and isinstance(widget, ItemWidget) and widget.isSelected():
                item = widget.item

        if item is not None:
            self.setItem(item)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 42 * x), round(self.position[1] + self.size[1] / 12 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 42 * w), round(self.size[1] / 12 * h)

    def setItem(self, item):
        self.widgets['outline'] = Rectangle(self.window, self.getPos(34, 0), self.getSize(8, 12), Color.WHITE, 2)
        self.widgets['title'] = Text(self.window, self.getPos(34, 0), self.getSize(8, 2), Color.WHITE, i18n('items', item.name), 0.9)
        self.widgets['image'] = ItemWidget(self.window, self.getPos(35, 2), self.getSize(6, 6), item, Rules.GAME.inventory[item], Rules.GAME.levels.get(item))
        text = ''
        if item.enchantable:
            attribute = Level.getItemByName(item.name)
            value = attribute.val + attribute.upgrade * Rules.GAME.levels[item]
            if attribute.kind == 'duration' or attribute.kind == 'damage':
                text = f"{i18n('attribute', attribute.kind)} : {int(value)}"
            elif attribute.kind == 'armor':
                text = f"{i18n('attribute', attribute.kind)} : {int(value*100)}%"
        self.widgets['value'] = Text(self.window, self.getPos(35, 9), self.getSize(6, 2), Color.WHITE, text)