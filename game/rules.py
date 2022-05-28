class Rules:

    FPS = 120
    SCREEN_SIZE = (1280, 720)
    FULLSCREEN = False
    MUSIC = False
    SOUND = False
    SCREEN_ICON = 'assets/images/icon.png'
    WINDOW_TITLE = 'Minecraft Survival'
    BG_COLOR = None

    FONT = 'assets/font/iFlash502.ttf'
    LANG = 1

    MOB_RARITY = 1
    EFFECT_RARITY = 1
    CHEST_COST = 100

    NAME_SELECT = None
    KIND_SELECT = None

    GAME = None
    GAME_MOB = None
    GAME_EFFECT = None
    GAME_DIFFICULTY = None

    GRID_SIZE = (48, 27)
    GRID_COLOR = (150, 150, 150)
    RECT_COLOR = (0, 0, 0)

    PROBS = [
        0.1,  # common (1)
        0.05,  # rare (2)
        0.025,  # epic (3)
        0.0125  # legendary (4)
    ]