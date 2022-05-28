from data.enum.colors import Color
from data.enum.items import Item
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from widget._widget import Widget
from widget.button import Button
from widget.play.item import ItemWidget
from widget.rectangle import Rectangle
from widget.text import Text


class EnchantingWidget(Widget):

    def __init__(self, window, position, size):
        super().__init__(window, position, size)

        # size = (42, 12)

        self.widgets = {}

        self.item = None
        self.itemSet = False

        self.resetItems()

    def loop(self):
        super().loop()

        for widget in self.widgets.values():
            widget.loop()

            if Input.clic and widget.isSelected() and widget.playAnimWhenSelect and isinstance(widget, ItemWidget):
                self.itemSet = False
                self.item = widget.item

        if self.item is not None:
            if not self.itemSet:
                self.setItem(self.item)
            if self.widgets['enchantButton'].isSelected() and Input.clic and self.widgets['enchantButton'].playAnimWhenSelect:
                Rules.GAME.levels[self.item] = 1
                Rules.GAME.inventory[Item.EXPERIENCE_BOTTLE] -= 1
                self.item = None
                del self.widgets['enchantButton']
                del self.widgets['outline']
                del self.widgets['title']
                del self.widgets['image']
                del self.widgets['bottle']
                self.resetItems()

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 42 * x), round(self.position[1] + self.size[1] / 12 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 42 * w), round(self.size[1] / 12 * h)

    def setItem(self, item):
        self.itemSet = True
        self.widgets['outline'] = Rectangle(self.window, self.getPos(34, 0), self.getSize(8, 12), Color.WHITE, 2)
        self.widgets['title'] = Text(self.window, self.getPos(34, 0), self.getSize(8, 2), Color.WHITE, i18n('items', item.name), 0.9)
        self.widgets['image'] = ItemWidget(self.window, self.getPos(36.5, 2), self.getSize(3, 3), item, 1)
        self.widgets['bottle'] = ItemWidget(self.window, self.getPos(36.5, 6), self.getSize(3, 3), Item.EXPERIENCE_BOTTLE, 1)
        self.widgets['enchantButton'] = Button(self.window, self.getPos(34.5, 10), self.getSize(7, 2), i18n('enchant'))
        if Rules.GAME.inventory[Item.EXPERIENCE_BOTTLE] > 0:
            self.widgets['enchantButton'].setAnimSelect()

    def resetItems(self):
        coords = [(x * 3, y * 3) for x in range(11) for y in range(4)]

        for nb, item in enumerate(Item):
            if item != Item.EMPTY:
                if Rules.GAME.inventory[item] == 0:
                    self.widgets[f'item{item.name}'] = Rectangle(self.window, self.getPos(*coords[nb]), self.getSize(3, 3),
                                                                 Color.WHITE, 2)
                else:
                    if item.enchantable and Rules.GAME.levels[item] == 0:
                        self.widgets[f'item{item.name}'] = ItemWidget(self.window, self.getPos(*coords[nb]),
                                                                      self.getSize(3, 3), item, 1).setAnimSelect()
                    else:
                        self.widgets[f'item{item.name}'] = ItemWidget(self.window, self.getPos(*coords[nb]),
                                                                      self.getSize(3, 3), item, 0)