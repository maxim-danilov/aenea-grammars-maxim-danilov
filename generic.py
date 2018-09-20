from natlink import setMicState
from aenea import (
    Key,
    Text,
    Mouse,
)
from dragonfly import Function
from words import (
    cap_that,
    lower_that
)
import re


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.
    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.
    """
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")


letterMap = {
    "alpha": "a",
    "bravo": "b",
    "charlie": "c",
    "delta": "d",
    "echo": "e",
    "foxtrot": "f",
    "golf": "g",
    "hotel ": "h",
    "india": "i",
    "juliet": "j",
    "kilo ": "k",
    "lima": "l",
    "mike ": "m",
    "november": "n",
    "Oscar": "o",
    "papa": "p",
    "quebec": "q",
    "romeo": "r",
    "sierra": "s",
    "tango": "t",
    "uniform": "u",
    "victor": "v",
    "whiskey": "w",
    "x-ray ": "x",
    "yankee": "y",
    "zulu ": "z",
}

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backspace": "backspace"
}

specialCharMap = {
    # "(bar|vertical bar|pipe)": "|",
    "hyphen": "hyphen",
    "dot": "dot",
    "calm": "comma",
    "backslash": "backslash",
    "tilde": "tilde",
    # "underscore": "_",
    # "asterisk": "*",
    # "colon": ":",
    # "semi-col": ";",
    # "at symbol": "@",
    # "[double] quote": """,
    "single quote": "squote",
    # "pound|hash": "#",
    # "dollar": "$",
    # "percent": "%",
    # "and": "&",
    "slash": "slash",
    "equals": "equal",
    "plus": "plus",
    "quest mark": "question",
}

release = Key("shift:up, ctrl:up, alt:up, win:up")

# Modifiers for the press-command.
modifierMap = {
    "alt|option": "a",
    "control": "c",
    "shift": "s",
    "command|cod": "w",
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(specialCharMap)

# These words can be prefaced by the word "say"
reservedWord = {
    "up": "up ",
    "down": "down ",
    "left": "left ",
    "right": "right ",
    "space": "space ",
    "tab": "tab ",
    "backspace": "backspace ",
    "delete": "delete ",
    "enter": "enter ",
    "paste": "paste ",
    "copy": "copy ",
    "cut": "cut ",
    "scratch": "scratch ",
    "undo": "undo ",
    "release": "release ",
    "page up": "page up ",
    "page down": "page down ",
    "say": "say ",
    "select": "select ",
    "uppercase": "uppercase ",
    "lowercase": "lowercase ",
    "dash": "dash ",
    "underscore": "underscore ",
    "dot": "dot ",
    "period": "period ",
    "minus": "minus ",
    "hyphen": "hyphen ",
    "kill": "kill ",
    "to end": "to end ",
    "slap": "slap ",
    "pound": "pound ",
    "hash": "hash ",
    "escape": "escape ",
    "hi": "Hi ",
    "semi": "semi ",
    "talk": "talk",
}

nonVimGenericKeys = {
    "say <text>": Function(lower_that),
    "cap <text>": Function(cap_that),
    "<specials> [repeat <n>]": Key("%(specials)s:%(n)d"),
}

specialKeys = {
    "ampersand": "ampersand",
    "apostrophe": "apostrophe",
    "asterisk": "asterisk",
    "at symbol": "at",
    "backslash": "backslash",
    "backtick": "backtick",
    "vertical bar": "bar",
    "caret": "caret",
    "colon": "colon",
    "calm": "comma",
    "dollar": "dollar",
    "dot": "dot",
    "semi": "semicolon",
    "quote": "dquote",
    "equals": "space, equal, space",
    "equal": "equal",
    "bang": "exclamation",
    "hash": "hash",
    "hyphen": "hyphen",
    "escape": "escape",
    "minus": "minus",
    "percent": "percent",
    "plus": "plus",
    "quest mark": "question",
    "slash": "slash",
    "single quote": "squote",
    "tilde": "tilde",
    "underscore": "underscore",
    "tab": "tab",
    "langle": "langle",
    "lace": "lbrace",
    "lack": "lbracket",
    "(lap|lape)": "lparen",
    "rangle": "rangle",
    "race": "rbrace",
    "rack": "rbracket",
    "rap": "rparen",
}

genericKeys = {
    "release all": release,
    "press shift": Key("shift:down"),
    "release shift": Key("shift:up"),
    "press <pressKey>": Key("%(pressKey)s"),
    "say <reservedWord>": Text("%(reservedWord)s"),

    # Navigation keys.
    "<modifier1> <pressKey> [<n>]":
        Key("%(modifier1)s-%(pressKey)s:%(n)d"),
    "<modifier1> <modifier2> <pressKey> [<n>]":
        Key("%(modifier1)s%(modifier2)s-%(pressKey)s:%(n)d"),

    "add omni task": Key("ca-space"),  # Add task with quick and entry to omnifocus
    "tick": Mouse("left"),
    "dooble": Mouse("left:2"),
    "tock": Mouse("right"),
    "dragon snore": Function(cancel_and_sleep),
}
