from util.anchor import Anchor


class Box:

    """
    Rectangle de widget
    """

    def __init__(self, rect, size, anchor=Anchor.CENTER):
        """
        rect: rectangle de définition
        size: dimensions du widget (boite de collision)
        anchor: ancrage
        """

        self.rect = rect
        self.size = size
        self.anchor = anchor

        self.prePos = self.rect.x, self.rect.y

        self.position = self.prePos
        self.setAnchor()

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def w(self):
        return self.size[0]

    @property
    def h(self):
        return self.size[1]

    def setAnchor(self):
        dx = (self.rect.w - self.w) // 2
        dy = (self.rect.h - self.h) // 2

        self.position = self.rect.x + self.anchor.x * dx, self.rect.y + self.anchor.y * dy

    def setPosition(self, position):

        x, y = position

        dx = (x - self.rect.x)
        dy = (y - self.rect.y)

        self.rect.x += dx
        self.rect.y += dy

        px, py = self.position
        self.position = px + dx, py + dy