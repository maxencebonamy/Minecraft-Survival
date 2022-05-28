import pygame

from game.rules import Rules
from input.input import Input
from output.output import Output


class Main:

    """
    Classe principale
    """

    def __init__(self):
        """
        input: évenenements d'entrée (clavier, souris)
        output: sortie (affichage, son)
        """

        self.input = Input()
        self.output = Output()

    def loop(self):
        """
        Boucle principale
        """

        # boucle des entrées et sorties
        self.input.loop()
        self.output.loop()

        # gestion des images par seconde
        fps = Rules.FPS
        pygame.time.wait(1000 // fps)


# initialisation de pygame
pygame.init()

# instance de la classe principale
main = Main()

# exécuter le programme tant que run est vrai
run = True

while run:

    main.loop()

    if main.input.close:
        run = False
        pygame.quit()