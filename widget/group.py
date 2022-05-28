from widget._widget import Widget


class GroupWidget(Widget):

    def __init__(self, window, position, size, widgets):
        super().__init__(window, position, size)
        self.widgets = widgets

        self.dx = [widget.x - self.x for widget in self.widgets]
        self.dy = [widget.y - self.y for widget in self.widgets]

    def loop(self):
        super().loop()

        for widget in self.widgets:
            widget.loop()

    def setPosition(self, position):
        super().setPosition(position)
        x, y = position

        for index, widget in enumerate(self.widgets):
            widget.setPosition((x + self.dx[index], y + self.dy[index]))