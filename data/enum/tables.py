from enum import Enum

from images import Import


class Table(Enum):

    # NAME = ('name', image)

    INVENTORY = ('inventory', Import.TABLES.INVENTORY)
    CRAFTING_TABLE = ('crafting_table', Import.TABLES.CRAFTING_TABLE)
    ENCHANTING_TABLE = ('enchanting_table', Import.TABLES.ENCHANTING_TABLE)
    ANVIL = ('anvil', Import.TABLES.ANVIL)

    @property
    def name(self):
        return self.value[0]

    @property
    def image(self):
        return self.value[1]

    @staticmethod
    def getTableByName(name):
        for table in Table:
            if table.name == name:
                return table
        return None