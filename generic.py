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
    "(alpha|arch)": "a",
    "(bravo|brav) ": "b",
    "(charlie|turley|char) ": "c",
    "(delta|del) ": "d",
    "(echo|eck) ": "e",
    "(foxtrot|fox) ": "f",
    "(golf|gang) ": "g",
    "(hotel) ": "h",
    "(india|indigo|ish) ": "i",
    "(juliet|julia) ": "j",
    "(kilo) ": "k",
    "(lima|lion|line|lie) ": "l",
    "(mike) ": "m",
    "(november|noy) ": "n",
    "(Oscar|osh) ": "o",
    "(papa|poppa|pom) ": "p",
    "(quebec|quiche|queen) ": "q",
    "(romeo|ree) ": "r",
    "(sierra|soy) ": "s",
    "(tango|tay) ": "t",
    "(uniform|umm) ": "u",
    "(victor|van) ": "v",
    "(whiskey|wes) ": "w",
    "(x-ray) ": "x",
    "(yankee|yaa) ": "y",
    "(zulu) ": "z",
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

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
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
    # Input text
    "say <text>": Function(lower_that),
    "cap <text>": Function(cap_that),
    "<letters>": Key("%(letters)s"),
    "sky <letters>": Key("s-%(letters)s"),
    "num <numbers>": Key("%(numbers)s"),
    "<numbers>": Key("%(numbers)s"),
    "<specials> [repeat <n>]": Key("%(specials)s:%(n)d"),

    # Cursor manipulation
    'up [<n>]': Key('up:%(n)d'),
    'down [<n>]': Key('down:%(n)d'),
    'left [<n>]': Key('left:%(n)d'),
    'right [<n>]': Key('right:%(n)d'),

    # Page buttons
    'gope [<n>]': Key('pgup:%(n)d'),
    'drop [<n>]': Key('pgdown:%(n)d'),

    # Word selection
    'lope [<n>]': Key('c-left:%(n)d'),
    'yope [<n>]': Key('c-right:%(n)d'),

    # Delete text
    'chuck [<n>]': Key('del:%(n)d'),
    'scratch [<n>]': Key('backspace:%(n)d'),
    'bump [<n>]': Key('cs-right:%(n)d, del'),
    'whack [<n>]': Key('cs-left:%(n)d, del'),
    'strip': Key('s-end:2, del'),
    'striss': Key('s-home:2, del'),
    'wipe [<n>]': Key('home, shift:down, end, shift:up, del'),

    # Home and end
    'care': Key('home'),
    'doll': Key('end'),
    'file top': Key('c-home'),
    'file toe': Key('c-end'),

    # Common buttons
    'tab [<n>]': Key('tab:%(n)d'),
    'ace [<n>]': Key('space:%(n)d'),
    'slap [<n>]': Key('enter:%(n)d'),
    'act': Key('escape'),

    # Clipboard
    'copy': Key('c-c'),
    'plop [<n>]': Key('c-v:%(n)d'),

    # Undo, redo
    'undo': Key('c-z'),
    'redo': Key('c-r'),

    # Navigation
    'back [<n>]': Key('a-left:%(n)d'),
    'level up [<n>]': Key('a-up:%(n)d'),

    # Select all
    'select all': Key('c-a'),
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

    # navigation keys.
    "page up [<n>]": Key("pgup:%(n)d"),
    "page down [<n>]": Key("pgdown:%(n)d"),

    # press keystroke
    "<modifier1> <pressKey> [<n>]": Key("%(modifier1)s-%(pressKey)s:%(n)d"),
    "<modifier1> <modifier2> <pressKey> [<n>]": Key("%(modifier1)s%(modifier2)s-%(pressKey)s:%(n)d"),

    # mouse buttons
    "tick": Mouse("left"),
    "dooble": Mouse("left:2"),
    "tock": Mouse("right"),

    "dragon snore": Function(cancel_and_sleep),
}
