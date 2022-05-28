from game.rules import Rules


class Animation:

    """
    Animation d'un widget
    """

    def __init__(self, widget, time):
        """
        :param widget: widget d'application de l'animation
        :param time: durée ou période de l'animation (sans accélération)

        position: position du widget

        """

        self.widget = widget
        self.time = time * Rules.FPS

        self.position = self.x, self.y = self.widget.position

        self.t = 0

        self.hasFinished = False