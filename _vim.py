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

letterMap  = {}
specialKeys = {}
numberMap = {}

findSymbolCharMap = {
    'foxtrot': 'f',
    'sky foxtrot': 'F',
    'tango': 't',
    'sky tango': 'T',
}

movementsCharMap = {
    'echo': 'e',
    'bravo': 'b',
    'whiskey': 'w',
    'sky echo': 'E',
    'sky bravo': 'B',
    'sky whiskey': 'W',

    'dollar': '$',
    'caret': '^',
    'zero': '0',

    'lace': '{',
    'race': '}',
}

visualCharMap = {
    'victor': 'v',
    'sky victor': 'V',
}

cutPasteCharMap = {
    'papa': 'p',
    'sky papa': 'P',
    'yankee': 'y',
    'sky yankee': 'Y',
    'delta': 'd',
    'delta delta': 'dd',
}

vimGeneric = {
    # d3f'
    # operate count find symbol
    # (d,c,y,v) (number=1) (f,t) (any alphabet/special)
    '<cutPasteCharMap> [<n>] <findSymbolCharMap> <letterMap>': Key("%(cutPasteCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(letterMap)s"),
    '<cutPasteCharMap> [<n>] <findSymbolCharMap> <specialKeys>': Key("%(cutPasteCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(specialKeys)s"),
    '<visualCharMap> [<n>] <findSymbolCharMap> <letterMap>': Key("%(visualCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(letterMap)s"),
    '<visualCharMap> [<n>] <findSymbolCharMap> <specialKeys>': Key("%(visualCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(specialKeys)s"),

    # v3e
    # operate count word-movement
    # (d,c,y,v) (number=1) (ebw)
    '<cutPasteCharMap> [<n>] <movementsCharMap>': Key("%(cutPasteCharMap)s") + Key("%(n)s") + Key("%(movementsCharMap)s"),
    '<visualCharMap> [<n>] <movementsCharMap>': Key("%(visualCharMap)s") + Key("%(n)s") + Key("%(movementsCharMap)s"),

    # v3ep
}

generalKeys = {}
# generalKeys.update(generic.genericKeys)
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
        # vim
        Choice("findSymbolCharMap", findSymbolCharMap),
        Choice("movementsCharMap", movementsCharMap),
        Choice("visualCharMap", visualCharMap),
        Choice("cutPasteCharMap", cutPasteCharMap),
        # generic
        Choice('letterMap', generic.letterMap),
        Choice('specialKeys', generic.specialKeys),
        Choice('numberMap', generic.numberMap),
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
    ProxyAppContext(match='regex', title='(?i).*(vim|pycharm|webstorm).*'),
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

