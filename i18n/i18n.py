from game.rules import Rules
from i18n import english, french


def i18n(*args):

    langs = (english.english, french.french)

    text = langs[Rules.LANG]

    for arg in args:
        text = text[arg]

    return text