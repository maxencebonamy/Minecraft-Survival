from game.rules import Rules
from output.sound import Sound
from output.window import Window


class Output:

    """
    Sortie (affichage, son)
    """

    def __init__(self):
        """
        window: fenêtre du jeu
        """

        self.window = Window()
        Sound.playMusic()

    def loop(self):
        """
        Boucle principale
        """

        self.window.loop()
        Sound.loop()