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
    # insert
    'india': Key('i'),
    'sky india': Key('I'),
    'alpha': Key('a'),
    'sky alpha': Key('A'),
    'Oscar': Key('o'),
    'sky Oscar': Key('O'),

    # screen/window
    'screen top': Key("z, t"),
    'screen (center|middle)': Key("z, dot"),
    'screen bottom': Key("z, b"),
    "switch screen": Key("c-w,w"),

    # search
    'find <text>': Text('/\c%(text)s'),
    "replace": Key("colon, percent, s, slash, slash, g, left, left"),
    'maru [<n>]': Key('%(n)d, asterisk'),
    'paru [<n>]': Key('%(n)d, hash'),

    # case
    'swap case': Text('~'),

    # macro
    'record macro': Text('qq'),
    'play macro': Text('@q'),
    'play macro two': Text('@w'),

    # my macro
    'inside string': Text('@u'),
    'inside bracket': Text('@y'),
    'replace string': Text('@up'),
    'replace bracket': Text('@yp'),

    # marks
    'mark that': Text('ma'),
    'jump mark': Text(''''a'''),

    # movements
    'go top': Text('gg'),
    'go bottom': Text('G'),
    'jump': Key('squote,squote'),

    # simple actions
    'remove line': Text('dd'),
    'rosh [<n>]': Key('d,%(n)d') + Key('e'),
    'dosh [<n>]': Key('d,%(n)d') + Key('b'),

    # actions chains:
    # d3f'
    '<cutPasteCharMap> [<n>] <findSymbolCharMap> <letterMap>': Key("%(cutPasteCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(letterMap)s"),
    '<cutPasteCharMap> [<n>] <findSymbolCharMap> <specialKeys>': Key("%(cutPasteCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(specialKeys)s"),
    '<visualCharMap> [<n>] <findSymbolCharMap> <letterMap>': Key("%(visualCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(letterMap)s"),
    '<visualCharMap> [<n>] <findSymbolCharMap> <specialKeys>': Key("%(visualCharMap)s") + Key("%(n)s") + Key("%(findSymbolCharMap)s") + Key("%(specialKeys)s"),

    # v3e
    '<cutPasteCharMap> [<n>] <movementsCharMap>': Key("%(cutPasteCharMap)s") + Key("%(n)s") + Key("%(movementsCharMap)s"),
    '<visualCharMap> [<n>] <movementsCharMap>': Key("%(visualCharMap)s") + Key("%(n)s") + Key("%(movementsCharMap)s"),

    # commands
    "exit vim": Key("colon,q,enter"),
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

