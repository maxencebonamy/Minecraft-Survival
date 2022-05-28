import pygame

from data.enum.keys import Key
from game.rules import Rules


class Input:

    """
    Entrée des évenements (clavier, souris)

    mouse: coordonnées de la souris
    keys: touches préssées du clavier
    close: bouton quitter de la fenêtre / touche quitter du clavier
    clic: clic droit de la souris
    resize: redimensionnement de la fenêtre
    """

    mouse = (0, 0)
    keys = []
    close = False
    clic = False
    resize = False

    def loop(self):
        """
        Boucle principale
        """

        # remettre les valeurs par défaut
        Input.close = False
        Input.clic = False
        Input.resize = False

        # parcourir les évenements actuels
        for event in pygame.event.get():

            # bouton quitter de la fenêtre
            if event.type == pygame.QUIT:
                Input.close = True

            # redimensionnement de la fenêtre
            elif event.type == pygame.VIDEORESIZE:
                Rules.SCREEN_SIZE = event.w, event.h
                Input.resize = True

            # mouvement de la souris
            elif event.type == pygame.MOUSEMOTION:
                Input.mouse = pygame.mouse.get_pos()

            # clic droit de la souris
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                Input.clic = True

            # touches préssées du clavier
            elif event.type == pygame.KEYDOWN:
                Input.keys.append(event.key)
                if event.key == pygame.K_ESCAPE:
                    Input.close = True
            elif event.type == pygame.KEYUP:
                Input.keys.remove(event.key)

        # touche quitter du clavier
        if Key.CLOSE in Input.keys:
            Input.close = True