import random

import pygame.mixer as mix

from game.rules import Rules

mix.pre_init(44100, -16, 2, 2048)

mix.init()


class Sound:

    BOW = mix.Sound('assets/sound/bow.mp3')
    BUTTON = mix.Sound('assets/sound/button.mp3')
    CHEST = mix.Sound('assets/sound/chest.mp3')
    DAMAGE = mix.Sound('assets/sound/damage.mp3')
    EAT = mix.Sound('assets/sound/eat.mp3')
    ELDER_GUARDIAN_DEATH = mix.Sound('assets/sound/elder_guardian_death.mp3')
    ELDER_GUARDIAN_SPAWN = mix.Sound('assets/sound/elder_guardian_spawn.mp3')
    END = mix.Sound('assets/sound/end.mp3')
    LEVEL = mix.Sound('assets/sound/level.mp3')
    ORB = mix.Sound('assets/sound/orb.mp3')
    PORTAL = mix.Sound('assets/sound/portal.mp3')
    POTION = mix.Sound('assets/sound/potion.mp3')
    WITHER_DEATH = mix.Sound('assets/sound/wither_death.mp3')
    WITHER_SPAWN = mix.Sound('assets/sound/wither_spawn.mp3')

    _music = None

    _MUSICS = (
        'assets/music/danny.mp3',
        'assets/music/dry_hands.mp3',
        'assets/music/equinoxe.mp3',
        'assets/music/haggstrom.mp3',
        'assets/music/living_mice.mp3',
        'assets/music/mice_on_venus.mp3',
        'assets/music/minecraft.mp3',
        'assets/music/moog_city.mp3',
        'assets/music/subwoofer_lullaby.mp3',
        'assets/music/sweden.mp3',
        'assets/music/wet_hands.mp3'
    )

    @staticmethod
    def loop():
        if not Rules.MUSIC:
            mix.music.stop()
            Sound._music = None
        elif not mix.music.get_busy():
            Sound.playMusic()

    @staticmethod
    def playSound(sound):
        if Rules.SOUND:
            sound.play()

    @staticmethod
    def playMusic():
        if Rules.MUSIC:
            music = Sound._drawMusic()
            Sound._music = music
            mix.music.load(music)
            mix.music.play()

    @staticmethod
    def _drawMusic():
        music = None
        while music is None or music == Sound._music:
            music = random.choice(Sound._MUSICS)
        return music

    @staticmethod
    def getMobSound(mob):
        return mix.Sound(f'assets/sound/mobs/{mob.name}.mp3')