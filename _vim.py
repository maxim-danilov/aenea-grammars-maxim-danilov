import generic
import words
from aenea import *

findSymbolCharMap = {
    'fox': 'f',
    'sky fox': 'F',
    'tay': 't',
    'sky tay': 'T',
}

movementsCharMap = {
    'eck': 'e',
    'brav': 'b',
    'wes': 'w',
    'sky eck': 'E',
    'sky brav': 'B',
    'sky wes': 'W',

    'dollar': '$',
    'caret': '^',
    'zero': '0',

    'lace': '{',
    'race': '}',
}

visualCharMap = {
    'van': 'v',
    'sky van': 'V',
}

cutPasteCharMap = {
    'pow': 'p',
    'sky pow': 'P',
    'yaa': 'y',
    'sky yaa': 'Y',
    'del': 'd',
    'sky del': 'D',
    'char': 'c',
    'sky char': 'C',
}

vimGeneric = {
    # insert mode
    'ice': Key('i'),
    'sky ice': Key('I'),
    'arch': Key('a'),
    'sky arch': Key('A'),
    'ork': Key('o'),
    'sky ork': Key('O'),

    # screen/window
    'screen top': Key('z, t'),
    'screen (center|middle)': Key('z, dot'),
    'screen bottom': Key('z, b'),
    'switch screen': Key('c-w,w'),

    # search
    'find <text>': Text('/\c%(text)s') + Pause('30') + Key('enter'),
    'bind <text>': Text('?\c%(text)s') + Pause('30') + Key('enter'),
    'replace': Key('colon, s, slash, slash, slash, g, left, left, left'),
    'maru [<n>]': Key('%(n)d, asterisk'),
    'paru [<n>]': Key('%(n)d, hash'),

    # case
    'swap case': Text('~'),

    # macro
    'record macro': Text('qq'),
    'play macro': Text('@q'),
    'play macro two': Text('@w'),

    # my macro
    'inside string': Text('f\'lvt\''),
    'inside bracket': Text('f(lvt)'),
    'replace string': Text('f\'lvt\'p'),
    'replace bracket': Text('f(lvt)p'),
    'select outside': Text('V$%%'),
    'select inside': Text('$v%%'),

    # marks
    'mark that': Text('ma'),
    'jump mark': Text(''''a'''),

    # movements
    'go top': Text('gg'),
    'go bottom': Text('G'),
    'jump': Key('squote,squote'),
    'line <line_number>': Text('%(line_number)dgg'),

    # simple actions
    'remove line [<n>]': Text('%(n)d') + Text('dd'),
    'select (line) [<n>]': Text('V') + (Key('down') + Pause('20')) * Repeat(extra='n'),
    'rosh [<n>]': Key('c,%(n)d') + Key('e'),
    'dosh [<n>]': Key('c,%(n)d') + Key('b'),

    # actions chains:
    # d3f'
    '<cutPasteCharMap> [<n>] <findSymbolCharMap> <letterMap>': Key('%(cutPasteCharMap)s') + Key('%(n)s') + Key('%(findSymbolCharMap)s') + Key('%(letterMap)s'),
    '<cutPasteCharMap> [<n>] <findSymbolCharMap> <specialKeys>': Key('%(cutPasteCharMap)s') + Key('%(n)s') + Key('%(findSymbolCharMap)s') + Key('%(specialKeys)s'),
    '<visualCharMap> [<n>] <findSymbolCharMap> <letterMap>': Key('%(visualCharMap)s') + Key('%(n)s') + Key('%(findSymbolCharMap)s') + Key('%(letterMap)s'),
    '<visualCharMap> [<n>] <findSymbolCharMap> <specialKeys>': Key('%(visualCharMap)s') + Key('%(n)s') + Key('%(findSymbolCharMap)s') + Key('%(specialKeys)s'),

    # v3e
    '<cutPasteCharMap> [<n>] <movementsCharMap>': Key('%(cutPasteCharMap)s') + Key('%(n)s') + Key('%(movementsCharMap)s'),
    '<visualCharMap> [<n>] <movementsCharMap>': Key('%(visualCharMap)s') + Key('%(n)s') + Key('%(movementsCharMap)s'),

    # tricks
    'char tay cube': Text('ct\''),
    'van ice cube': Text('vi\''),
    'van ice brav': Text('vib'),

    'select line <line_number> plus [<n>]': Text('%(line_number)dgg') + Text('V') + (Key('down') + Pause('20')) * Repeat(extra='n'),
    'remove outside': Text('V$%d'),

    # commands
    'exit vim': Key('colon,q,enter'),
    'registers': Key('colon') + Text('reg') + Key('enter'),

    # registers
    'insert <specialKeys>': Text('"') + Key('%(specialKeys)s') + Key('p'),
    'insert <letterMap>': Text('"') + Key('%(letterMap)s') + Key('p'),

    'put <letterMap>': Text('"') + Key('%(letterMap)s') + Key('y'),

    'start append copy': Text('"ay'),
    'append copy': Text('"Ay'),
}

generalKeys = {}
generalKeys.update(vimGeneric)

grammarCfg = Config('all')
grammarCfg.cmd = Section('Language section')
grammarCfg.cmd.map = Item(generalKeys,
                          namespace={
                              'Key': Key,
                              'Text': Text,
                          })

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef('n', 1, 65),
        IntegerRef('line_number', 1, 9999),
        Dictation('text'),
        # vim
        Choice('findSymbolCharMap', findSymbolCharMap),
        Choice('movementsCharMap', movementsCharMap),
        Choice('visualCharMap', visualCharMap),
        Choice('cutPasteCharMap', cutPasteCharMap),
        # generic
        Choice('letterMap', generic.letterMap),
        Choice('specialKeys', generic.specialKeys),
    ]
    defaults = {
        'n': 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=9, name='sequence')

class RepeatRule(CompoundRule):
    spec = '<sequence>'
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras['sequence']
        for action in sequence:
            action.execute()


vim_plus_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*(vim|pycharm|webstorm).*'),
    AppContext(title='Terminal')
)
grammar = Grammar('root rule', context = vim_plus_context)
grammar.add_rule(RepeatRule())
grammar.load()

def unload():
    '''Unload function which will be called at unload time.'''
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

