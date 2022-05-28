from animation.jump import JumpAnimation
from animation.linear import LinearAnimation
from data.enum.colors import Color
from data.enum.mobs import Mob
from output.sound import Sound
from util.screenCutting import ScreenCutting
from widget._widget import Widget
from widget.game.card import CardWidget
from widget.game.movePlayer import MovePlayerWidget
from widget.game.player import PlayerWidget
from widget.rectangle import Rectangle


class SetupCardsWidget(Widget):

    def __init__(self, window, position, size):
        super().__init__(window, position, size)

        self.cut = ScreenCutting(48, 27)
        x, y = self.cut.getOriginPos(*position)
        self.coords = [(x + 5 * index, y) for index in range(9)]
        self.cards = {}

        self.playerIndex = 5
        self.moves = []
        self.isAttacking = None

        self.highlighted = [index for index in range(1, 10)]

    def loop(self):
        super().loop()
        for index, widget in self.cards.items():
            if self.isAttacking is None or self.isAttacking != index:
                widget.loop()
        if self.isAttacking is not None:
            widget = self.cards[self.isAttacking]
            widget.loop()
            if not widget.animations:
                self.isAttacking = None

    def displayHighlighted(self):
        for index in self.highlighted:
            self.cards[index].loop()

    def setCard(self, index, widget, *args):
        self.cards[index] = widget(self.window, self.cut.getPos(*self.coords[index-1]), self.cut.getSize(4, 7), *args)

    def setMobs(self, mobs):
        for index in range(1, 10):
            mob = mobs.get(index)
            if mob is not None:
                self.setCard(index, CardWidget, mob)
            else:
                self.setCard(index, Rectangle, Color.WHITE, 2)

    def damage(self, index, hearts=1):
        if not isinstance(self.cards[index], Rectangle):
            self.cards[index].damage(hearts)
            if self.cards[index].healthBar.health == 0:
                if self.cards[index].mob == Mob.ELDER_GUARDIAN:
                    Sound.playSound(Sound.ELDER_GUARDIAN_DEATH)
                elif self.cards[index].mob == Mob.WITHER:
                    Sound.playSound(Sound.WITHER_DEATH)
                self.setCard(index, Rectangle, Color.WHITE, 2)

    def setPlayer(self, mob, position, distances):
        self.playerIndex = position
        self.moves = []

        self.removeAnimations()
        self.setCard(position, PlayerWidget, mob)
        for index in range(1, 10):
            if abs(position - index) in distances:
                self.setCard(index, MovePlayerWidget, mob)
                self.setAnimSelectCard(index)
                self.moves.append(index)
            elif index != position:
                self.setCard(index, Rectangle, Color.WHITE, 2)

    def attack(self, mobIndex, coords):
        self.isAttacking = mobIndex
        self.cards[mobIndex].animations.append(JumpAnimation(self.cards[mobIndex], 0.5, self.cut.getSize(0, 0.5)[1], 2))

    def highlight(self, position=5, distance=1):
        self.highlighted = []
        for index in range(1, 10):
            if abs(position - index) <= distance and not isinstance(self.cards[index], Rectangle):
                self.highlighted.append(index)

    def setAnimSelectCard(self, index, value=True):
        self.cards[index].setAnimSelect(value)

    def removeAnimations(self):
        for widget in self.cards.values():
            widget.setAnimSelect(False)