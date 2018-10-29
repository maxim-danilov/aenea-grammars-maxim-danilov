from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables

from aenea import *

# from dragonfly import Function
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')
import words
import generic
# import osx
# import r_vocab
# import vocab

esc = Key("escape")
LEADER = 'comma'
out = Key("escape:2,l")
ii = Key("i")

operateCharMap = {
    "parens": "rparen",
    "word": "w",
    "scent": "s",
    "para": "p",
    "bracks": "rbracket",
    "braces": "rbrace",
    "quotes": "dquote",
    "single quotes": "squote",
}

advCharMap = {
    "inner": "i",
    "around": "a",
}

verbCharMap = {
    "dosh": "d",
    "copy": "y",
    "change": "c",
    "select": "v",
}

lineVerbCharMap = {
    "dosh line": "d:2",
    "copy line": "y:2",
    "change line": "c:2,escape",
    "select line": "s-V",
    "kill till end": "s-D",
    "select till end": "v,dollar",
    "copy till end": "y,dollar",
    "change till end": "s-C,escape",
}

vimGeneric = {
    # inserting:
    # "<letters>": Key("%(letters)s"),
    # "sky <letters>": Key("s-%(letters)s"),
    # "num <numbers>": Key("%(numbers)s"),
    # "<numbers>": Key("%(numbers)s"),
    # "(ace|space) [repeat <n>]": Key("space:%(n)d"),
    # "<specials> [repeat <n>]": Key("%(specials)s:%(n)d"),
    # "say <text>": Function(lower_that),
    # "<text>": Function(lower_that),
    # "cap <text>": Function(cap_that),

    # "(slap|slop) [<n>]": Key("enter:%(n)d"),
    # "scratch [<n>]": Key("backspace:%(n)d"),
    # "kill [<n>]": Key("del:%(n)d"),

    "rosh [<n>]": esc + Key("%(n)d,d,l"),
    "dosh [<n>]": esc + Key("%(n)d,d,h"),

    # "[<n>] up": esc + Key("k:%(n)d"),
    # "[<n>] down": esc + Key("j:%(n)d"),
    # "[<n>] left": esc + Key("h:%(n)d"),
    # "[<n>] right": esc + Key("l:%(n)d"),

    #    "gee up [<n>]": esc + Text("%(n)d") + Key("g,k"),
    #    "gee down [<n>]": esc + Text("%(n)d") + Key("g,j"),
    #    "gee left [<n>]": esc + Text("%(n)d") + Key("g,h"),
    #    "gee right [<n>]": esc + Text("%(n)d") + Key("g,l"),

    # "[<n>] upper": Key("up:%(n)d"),
    # "[<n>] downer": Key("down:%(n)d"),
    # "[<n>] lefter": Key("left:%(n)d"),
    # "[<n>] righter": Key("right:%(n)d"),

    # "cary": Key("0"), CARE
    "car": Key("caret"),
    # "doll": Key("dollar"), DOLLAR
    "go to top": esc + Key("g,g"),
    "go to bottom": esc + Key("s-G"),

    "duplicate line [<n>]": esc + Key("y,y,p:%(n)d"),
    # "duplicate line above <n>": esc + Key("y,y,P:%(n)d"),

    "vis-mode": Key("v"),
    "vis-line": Key("s-v"),

    # "sert": esc + Key("i"), INDIA
    # "big sert": esc + Key("s-i"), SKY INDIA
    # "append": esc + Key("a"), ALPHA
    # "big append": esc + Key("s-a"), SKY ALPHA
    # "scape|escape|act": Key("escape"), ACT
    # "open": esc + Key("o"), OSCAR
    # "big open": esc + Key("s-o"),
    # "paste": esc + Key("p"), PAPA
    # "big paste": esc + Key("s-p"),

    "next [<n>]": Key("n:%(n)d"),
    "preeve [<n>]": Key("N:%(n)d"),

    # 'match that': esc + Key("percent"),

    '[<n>] rope': Key('%(n)d, w'),
    '[<n>] irope': Key('%(n)d, e'),
    '[<n>] lope': Key('%(n)d, b'),  # TODO: resolve the conflict with generic
    '[<n>] ilope': Key('%(n)d, g, e'),

    '[<n>] ropert': Key('%(n)d, s-W'),
    '[<n>] iropert': Key('%(n)d, s-E'),
    '[<n>] lopert': Key('%(n)d, s-B'),
    '[<n>] ilopert': Key('%(n)d, g, s-E'),

    'skip [<n>]': esc + Key("%(n)d, f"),
    'skip back [<n>]': esc + Key("%(n)d, s-F"),
    'grip [<n>]': esc + Key("%(n)d, t"),
    'grip back [<n>]': esc + Key("%(n)d, s-T"),

    "join [<n>]": esc + Key("s-J:%(n)d"),

    # Magic:
    # "<verbKey> <advKey> <opKey>": esc + Key("%(verbKey)s") + Key("%(advKey)s") + Key("%(opKey)s"),
    "dosh [<n>] (words|word)": Key("d,%(n)d") + Key("b"),
    "rosh [<n>] (words|word)": Key("d,%(n)d") + Key("e"),
    "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),
    "<verbKey>": Key("%(verbKey)s"),

    # "find": esc + Key("slash"),
    "find back": esc + Key("question"),
    # "jump till <text>": esc + Key("slash") + Text("%(text)s") + Key("enter"),

    # "mark that": esc + Key("m,a"),
    # "jump mark": esc + Key("backtick,a"),

    # TODO: fix that
    "switch": Key("squote,squote"),

    # "record macro": esc + Key("q,q"),
    # "end macro": Key("q"),
    # "repeat macro [<n>]": Key("%(n)d,at,q"),

    # "(maru) [<n>]": esc + Key("%(n)d, asterisk"),
    # "(paru) [<n>]": esc + Key("%(n)d, hash"),

}

# class vimCommands(MappingRule):
#     mapping  = {
#     }

generalKeys = {}
generalKeys.update(generic.genericKeys)
# generalKeys.update(osx.osx)
# generalKeys.update(vocab.vocabWord)
generalKeys.update(vimGeneric)

grammarCfg = Config("all")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(generalKeys,
                          namespace={
                              "Key": Key,
                              "Text": Text,
                          })

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 65),
        Dictation("text"),
        Choice("modifier1", generic.modifierMap),
        Choice("modifier2", generic.modifierMap),
        Choice('letters', generic.letterMap),
        Choice('letters2', generic.letterMap),
        Choice('specials', generic.specialKeys),
        Choice('numbers', generic.numberMap),
        Choice("pressKey", generic.pressKeyMap),
        Choice("reservedWord", generic.reservedWord),
        Choice("opKey", operateCharMap),
        Choice("advKey", advCharMap),
        Choice("verbKey", verbCharMap),
        Choice("lineVerbKey", lineVerbCharMap),
    ]
    defaults = {
        "n": 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=9, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()


vim_plus_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*(vim|pycharm).*'),
    AppContext(title='Terminal')
)
grammar = Grammar("root rule", context = vim_plus_context)
grammar.add_rule(RepeatRule())
grammar.load()

# exmode_grammar = Grammar("ExMode grammar",context=vim_plus_context)
# exmode_grammar.add_rule(vimCommands())
# exmode_grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

    global exmode_grammar
    if exmode_grammar:
        exmode_grammar.unload()
    exmode_grammar = None

