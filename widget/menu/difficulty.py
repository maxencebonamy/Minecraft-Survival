from data.enum.colors import Color
from game.rules import Rules
from i18n.i18n import i18n
from widget._widget import Widget
from widget.group import GroupWidget
from widget.rectangle import Rectangle
from widget.text import Text


class DifficultyWidget(Widget):

    def __init__(self, window, position, size, difficulty):
        super().__init__(window, position, size)

        mobs = difficulty.rounds
        tr = difficulty.trophies

        texts = (
            f"{i18n('steps')} : {difficulty.maxStep}",
            f"{i18n('title', 'mob')} : {mobs[0]} / {mobs[1]}",
            f"{i18n('emerald')} : {difficulty.emerald}",
            f"{i18n('attribute', 'trophy')} : {tr[0]} / {tr[1]}",
        )

        self.widget = GroupWidget(self.window, self.position, self.size, (
            Rectangle(self.window, self.getPos(0, 0), self.getSize(12, 8), Color.FG_DARK),
            Rectangle(self.window, self.getPos(0, 0), self.getSize(12, 10), Color.WHITE, 2),
            Rectangle(self.window, self.getPos(0, 2), self.getSize(12, 0), Color.WHITE, 2),
            Rectangle(self.window, self.getPos(0, 8), self.getSize(12, 0), Color.WHITE, 2),
            Text(self.window, self.getPos(0, 8), self.getSize(12, 2), Color.WHITE, i18n('playTitles', 'difficulty')),
            Text(self.window, self.getPos(0, 0), self.getSize(12, 2), Color.WHITE, i18n('difficulties', difficulty.name)),

            Text(self.window, self.getPos(0, 2), self.getSize(12, 1.5), Color.WHITE, texts[0], 0.9),
            Text(self.window, self.getPos(0, 3.5), self.getSize(12, 1.5), Color.WHITE, texts[1], 0.9),
            Text(self.window, self.getPos(0, 5), self.getSize(12, 1.5), Color.WHITE, texts[2], 0.9),
            Text(self.window, self.getPos(0, 6.5), self.getSize(12, 1.5), Color.WHITE, texts[3], 0.9),
        ))

    def loop(self):
        super().loop()
        self.widget.loop()

    def setPosition(self, position):
        super().setPosition(position)
        self.widget.setPosition(position)

    def getPos(self, x, y):
        return round(self.position[0] + self.size[0] / 12 * x), round(self.position[1] + self.size[1] / 10 * y)

    def getSize(self, w, h):
        return round(self.size[0] / 12 * w), round(self.size[1] / 10 * h)