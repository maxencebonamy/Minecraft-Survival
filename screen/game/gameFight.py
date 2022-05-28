import random

from data.enum.colors import Color
from data.enum.effects import Effect
from data.enum.items import Item
from data.enum.level import Level
from data.enum.mobs import Mob
from game.rules import Rules
from i18n.i18n import i18n
from input.input import Input
from output.sound import Sound
from save import Save
from screen._screen import Screen
from widget.bar import Bar
from widget.button import Button
from widget.game.effect import EffectWidget
from widget.game.hotBar import HotBarWidget
from widget.game.infoCard import InfoCardWidget
from widget.game.setupCards import SetupCardsWidget
from widget.group import GroupWidget
from widget.image import Image
from widget.play.healthBar import HealthBar
from widget.rectangle import Rectangle
from widget.text import Text


class GameFightScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        Rules.GAME.screen = 'gameFight'

        Rules.BG_COLOR = Color.BG_DARK

        self.effect = Rules.GAME_EFFECT
        self.effectLevel = Save.read(Save.getPath('effect', self.effect.name))
        self.effectRemain = self.effect.uses + self.effectLevel if self.effect.uses > 0 else 0
        self.effects = {effect: duration for effect, duration in Rules.GAME_MOB.effects.items() if duration < 0}

        self.isPlaying = True
        self.position = 5

        self.weapon = None
        self.isTargeting = None

        self.protection = self.getProtection()
        self.damage = self.getDamage('sword')
        self.bowDamage = self.getDamage('bow')
        self.fireDuration = self.getDamage('flint_and_steel')

        self.mobHealths = {}
        self.mobEffects = {}
        self.mob = Rules.GAME_MOB
        self.mobLevel = Save.read(Save.getPath('mob', self.mob.name))

        self.overlayRound = 40
        self.overlayMob = None

        self.widgets = {
            'healthBar': HealthBar(window, self.cut.getPos(15, 20), self.cut.getSize(18, 3),
                                   self.mob.health + 10 + self.mobLevel,
                                   (18, 3)),
            'progressionBar': Bar(window, self.cut.getPos(2, 1), self.cut.getSize(44, 2), 0),

            # 'next': Button(window, self.cut.getPos(38, 1), self.cut.getSize(8, 2), 'next').setAnimSelect(),

            'playerCards': SetupCardsWidget(window, self.cut.getPos(2, 12), self.cut.getSize(44, 7)),
            'mobsCards': SetupCardsWidget(window, self.cut.getPos(2, 4), self.cut.getSize(44, 7)),

            'useEffect': Button(window, self.cut.getPos(34, 24), self.cut.getSize(6, 2), 'use').setAnimSelect(),
            'effectCover': GroupWidget(window, self.cut.getPos(41, 20), self.cut.getSize(5, 6), (
                Rectangle(window, self.cut.getPos(41, 20), self.cut.getSize(5, 6), Color.RARITY[self.effect.rarity]),
                Image(window, self.cut.getPos(41.25, 20.25), self.cut.getSize(4.5, 5.5), self.effect.image),
                Rectangle(window, self.cut.getPos(41, 20), self.cut.getSize(5, 6), Color.WHITE, 2),
            )),

            'hotBar': HotBarWidget(self.window, self.cut.getPos(15, 24), self.cut.getSize(18, 2)),
        }

        self.bgOpacity = Rectangle(window, (0, 0), self.cut.getSize(48, 27), Color.BLACK).setOpacity(180)

        self.updateHotBar()
        self.updatePlayer()
        self.updateProgressionBar()
        self.updateMobs()
        self.updateEffectCount()
        self.updateEffects()

    def loop(self):
        super().loop()

        if self.overlayRound is not None:
            self.overlayRound -= 1
            if not self.widgets.get('overlay'):
                self.widgets['overlay'] = GroupWidget(self.window, self.cut.getPos(0, 5), self.cut.getSize(48, 17), (
                    Rectangle(self.window, (0, 0), self.cut.getSize(48, 27), Color.BLACK).setOpacity(180),
                    Text(self.window, self.cut.getPos(4.5, 5.5), self.cut.getSize(40, 17), Color.BLACK,
                         f"{i18n('round')} {Rules.GAME.round}"),
                    Text(self.window, self.cut.getPos(4, 5), self.cut.getSize(40, 17), Color.WHITE,
                         f"{i18n('round')} {Rules.GAME.round}")
                ))
            if self.overlayRound == 0:
                del self.widgets['overlay']
                self.overlayRound = None

        elif self.overlayMob is not None:
            if not self.widgets.get('overlay'):
                index = self.overlayMob
                mob = Rules.GAME.mobs[Rules.GAME.round - 1][index]
                self.widgets['overlay'] = GroupWidget(self.window, self.cut.getPos(17, 6.5), self.cut.getSize(14, 14), (
                    Rectangle(self.window, (0, 0), self.cut.getSize(48, 27), Color.BLACK).setOpacity(180),
                    InfoCardWidget(self.window, self.cut.getPos(17, 6.5), self.cut.getSize(14, 14), mob,
                                   self.mobHealths.get(index), self.mobEffects.get(index))
                ))
            if Input.clic:
                del self.widgets['overlay']
                self.overlayMob = None

        elif self.weapon is not None:
            self.bgOpacity.loop()
            distance, damage, effect, time = self.weapon
            widget = self.widgets['mobsCards']
            widget.highlight(self.position, distance)
            widget.displayHighlighted()
            if Effect.STRENGTH in self.effects:
                damage += 1
            if Input.clic:
                hasAttacked = False
                for index in widget.highlighted:
                    if widget.cards[index].isSelected():
                        Sound.playSound(Sound.getMobSound(Rules.GAME.mobs[Rules.GAME.round - 1][index]))
                        self.mobHealths[index] -= damage
                        self.widgets['mobsCards'].damage(index, damage)
                        if distance == 2:
                            item, nb, level = Rules.GAME.hotBar['arrow']
                            Rules.GAME.hotBar['arrow'] = item, nb - 1, level
                            self.updateHotBar()
                            Sound.playSound(Sound.BOW)
                        hasAttacked = True
                        if effect is not None:
                            self.addEffectMob(index, effect, time)
                            if distance != 0:
                                self.effectRemain -= 1
                                self.updateEffects()
                                self.updateEffectCount()
                                hasAttacked = False
                self.weapon = None
                if hasAttacked:
                    self.attack()
                    self.nextRound()

        else:
            if Input.clic:
                for name in [name for name in self.widgets.keys() if 'overlay' in name]:
                    del self.widgets[name]

                for index, card in self.widgets['mobsCards'].cards.items():
                    if card.isSelected() and self.isPlaying and not isinstance(card, Rectangle):
                        self.overlayMob = index

            self.loopMobs()
            self.loopPlayer()

            for index, case in self.widgets['hotBar'].cases.items():
                if case.isSelected() and Input.clic and self.isPlaying and not case.item == Item.EMPTY:
                    nb = Rules.GAME.hotBar['golden_apple'][1]
                    if index == 5:
                        self.target(0, self.damage)
                    elif index == 6 and Rules.GAME.hotBar['arrow'][1] and Rules.GAME.hotBar['arrow'][1] > 1:
                        self.target(2, self.bowDamage)
                    elif index == 7:
                        self.target(1, 0, Effect.FIRE, self.fireDuration)
                    elif index == 9 and nb > 0:
                        Rules.GAME.hotBar['golden_apple'] = (Item.GOLDEN_APPLE, nb - 1, 0)
                        self.addEffectPlayer(Effect.REGENERATION, 10)
                        self.widgets['healthBar'].setAbsorption(8)
                        self.updateEffects()
                        self.updateHotBar()
                        Sound.playSound(Sound.EAT)

            if self.widgets.get('next') in self.clicWidgets:
                if Rules.GAME.round < Rules.GAME.difficulty.rounds:
                    Rules.GAME.round += 1
                    self.updateProgressionBar()
                    self.updateMobs()
                else:
                    Rules.GAME.victory = True
                    self.nextScreen = 'gameEnd'
            if self.widgets['useEffect'] in self.clicWidgets and self.effectRemain > 0:
                Sound.playSound(Sound.POTION)
                if self.effect == Effect.ABSORPTION:
                    self.widgets['healthBar'].setAbsorption(4)
                    self.effectRemain -= 1
                    self.updateEffectCount()
                elif self.effect.onSelf:
                    self.addEffectPlayer(self.effect, self.effect.duration)
                    self.effectRemain -= 1
                    self.updateEffects()
                    self.updateEffectCount()
                    self.updatePlayer()
                else:
                    self.target(1, 0, self.effect, self.effect.duration)

    def nextRound(self):
        i = 0
        for index in range(1, 10):
            if isinstance(self.widgets['mobsCards'].cards[index], Rectangle):
                i += 1
        if i == 9:
            if Rules.GAME.round < Rules.GAME.difficulty.rounds:
                Rules.GAME.round += 1
                self.updateProgressionBar()
                self.updateMobs()
                self.overlayRound = 40
            else:
                Rules.GAME.victory = True
                self.nextScreen = 'gameEnd'

    def updateProgressionBar(self):
        percent = (Rules.GAME.round - 1) / Rules.GAME.difficulty.rounds
        self.widgets['progressionBar'] = Bar(self.window, self.cut.getPos(2, 1), self.cut.getSize(44, 2), percent)

    def updateMobs(self):
        self.mobHealths = {}
        mobs = Rules.GAME.mobs[Rules.GAME.round - 1]
        for index in range(1, 10):
            mob = mobs.get(index)
            if mob is not None:
                self.mobHealths[index] = mob.health
                self.mobEffects[index] = {effect: duration for effect, duration in mob.effects.items() if duration < 0}
        self.widgets['mobsCards'].setMobs(mobs)

        if Rules.GAME.mobs[Rules.GAME.round - 1].get(5):
            if Rules.GAME.mobs[Rules.GAME.round - 1][5] == Mob.ELDER_GUARDIAN:
                Sound.playSound(Sound.ELDER_GUARDIAN_SPAWN)
            elif Rules.GAME.mobs[Rules.GAME.round - 1][5] == Mob.WITHER:
                Sound.playSound(Sound.WITHER_SPAWN)

    def updatePlayer(self):
        if Effect.JUMP_BOOST in self.effects.keys():
            distances = [2]
        elif Effect.SPEED in self.effects.keys():
            distances = [1, 2]
        elif Effect.TELEPORT in self.effects.keys():
            distances = [1, 2, 3, 4, 5, 6, 7, 8]
        else:
            distances = [1]
        self.widgets['playerCards'].setPlayer(Rules.GAME_MOB, self.position, distances)

    def updateEffectCount(self):
        text = f'{self.effectRemain}/{self.effect.uses + self.effectLevel}'
        if self.effect.uses == 0:
            text = f'0/0'
        self.widgets['effectCount'] = GroupWidget(self.window, self.cut.getPos(34, 20), self.cut.getSize(6, 3), (
            Text(self.window, self.cut.getPos(34, 20), self.cut.getSize(6, 3), Color.WHITE, text, 0.8),
            Rectangle(self.window, self.cut.getPos(34, 20), self.cut.getSize(6, 3), Color.WHITE, 2)
        ))

    def updateEffects(self):
        coords = [(2 + x * 4, 20 + y * 2) for y in range(3) for x in range(3)]
        widgets = []
        i = 0
        for effect, duration in self.effects.items():
            widgets.append(
                EffectWidget(self.window, self.cut.getPos(*coords[i]), self.cut.getSize(4, 2), effect, duration))
            i += 1
        self.widgets['effects'] = GroupWidget(self.window, self.cut.getPos(2, 20), self.cut.getSize(12, 6), widgets)

    def updateHotBar(self):
        self.widgets['hotBar'].setHotBar(Rules.GAME.hotBar)

    def loopMobs(self):
        setup = self.widgets['mobsCards']
        if not self.isPlaying and setup.isAttacking is None:
            self.isPlaying = True

    def loopPlayer(self):
        setup = self.widgets['playerCards']
        if self.isPlaying:
            for index, widget in setup.cards.items():
                if Input.clic and index in setup.moves and widget.isSelected():
                    self.position = index
                    self.updatePlayer()
                    self.attack()

    def getPositionCard(self, position, adv=True):
        y = 4 if adv else 12
        x = (position - 1) * 5 + 2
        return x, y

    def attack(self):
        self.isPlaying = False
        mobs = Rules.GAME.mobs[Rules.GAME.round - 1]

        player = self.widgets['playerCards']
        canAttack = [index for index, mob in mobs.items() if abs(player.playerIndex - index) <= mob.distance and
                     not isinstance(self.widgets['mobsCards'].cards[index], Rectangle) and not (
                    self.mobEffects.get(index)
                    and ((Effect.NAUSEA in self.mobEffects[index].keys() and index != player.playerIndex)
                         or Effect.BLINDNESS in self.mobEffects[index].keys()))]
        if canAttack and Effect.INVISIBILITY not in self.effects:
            index = random.choice(canAttack)
            Sound.playSound(Sound.getMobSound(Rules.GAME.mobs[Rules.GAME.round - 1][index]))
            self.widgets['mobsCards'].attack(index, self.cut.getPos(*player.coords[player.playerIndex - 1]))
            damage = mobs[index].damage * self.protection
            if (Effect.RESISTANCE in self.effects or (
                    self.mobEffects.get(index) and Effect.WEAKNESS in self.mobEffects[index])) \
                    and self.widgets['healthBar'].health > 0.5:
                damage -= 1
            self.widgets['healthBar'].damage(damage)
            if self.widgets['healthBar'].health == 0:
                self.nextScreen = 'gameEnd'
            for effect, duration in mobs[index].effects.items():
                if effect.onSelf:
                    self.addEffectMob(index, effect, duration)
                else:
                    self.addEffectPlayer(effect, duration)
        else:
            self.isPlaying = True

        self.manageEffects()

    def manageEffects(self):
        healthBar = self.widgets['healthBar']

        for effect, duration in list(self.effects.items()):
            if effect == Effect.BLOW_UP:
                for i in range(self.position - 1, self.position + 2):
                    if 1 <= i <= 9:
                        self.widgets['mobsCards'].damage(i, 10)
            elif effect == Effect.FIRE:
                if Effect.FIRE_RESISTANCE not in self.effects.keys():
                    rd = random.randint(0, 1)
                    if rd:
                        healthBar.damage()
            elif effect == Effect.POISON:
                healthBar.damage()
            elif effect == Effect.INSTANT_HEALTH:
                healthBar.heal(2)
            elif effect == Effect.REGENERATION:
                healthBar.heal()

            if duration == 1:
                del self.effects[effect]
            else:
                self.effects[effect] -= 1

        for index, effects in list(self.mobEffects.items()):
            for effect, duration in list(effects.items()):
                if effect == Effect.BLOW_UP:
                    healthBar.damage(10)
                    for i in range(self.position - 1, self.position + 2):
                        if 1 <= i <= 9:
                            self.widgets['mobsCards'].damage(i, 10)
                elif effect == Effect.FIRE:
                    if Effect.FIRE_RESISTANCE not in self.mobEffects[index].keys():
                        rd = random.randint(0, 1)
                        if rd:
                            self.widgets['mobsCards'].damage(index)
                elif effect == Effect.POISON:
                    self.widgets['mobsCards'].damage(index)
                elif effect == Effect.INSTANT_DAMAGE:
                    self.widgets['mobsCards'].damage(index, 2)

                if duration == 1:
                    del self.mobEffects[index][effect]
                else:
                    self.mobEffects[index][effect] -= 1

        self.updateEffects()
        self.updatePlayer()

        self.nextRound()

        if self.widgets['healthBar'].health == 0:
            self.nextScreen = 'gameEnd'

    def target(self, distance, damage, effect=None, time=0):
        self.weapon = (distance, damage, effect, time)

    def addEffectPlayer(self, effect, duration):
        self.effects[effect] = duration
        self.updateEffects()

    def addEffectMob(self, index, effect, duration):
        if self.mobEffects.get(index) is None:
            self.mobEffects[index] = {effect: duration}
        else:
            self.mobEffects[index][effect] = duration

    def getProtection(self):
        i = 0
        for item, _, level in list(Rules.GAME.hotBar.values())[0:4]:
            if item is not None:
                attribute = Level.getItemByName(item.name)
                value = attribute.val + attribute.upgrade * level
                i += value
            else:
                i += 1
        return i / 4

    def getDamage(self, kind):
        item, _, level = Rules.GAME.hotBar[kind]
        if item is None:
            return 0
        attribute = Level.getItemByName(item.name)
        return attribute.val + attribute.upgrade * level
