import aenea.config
import aenea.configuration

from aenea import (
    AeneaContext,
    AppContext,
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    ProxyAppContext,
    Text
    )

grammar = Grammar('hello world aenea')

print 'Aenea hello world grammar: Loaded.'

class TestRule(MappingRule):
    mapping = {
          # Window switcher
          'window':         Key('a-space'),
          'window <n>':         Key('c-f1:%(n)d'),

          'fullscreen':         Key('f11'),

          # windows resize
          'window up': Key('control:down, win:down, up, control:up, win:up'),
          'window left': Key('control:down, win:down, left, control:up, win:up'),
          'window right': Key('control:down, win:down, right, control:up, win:up'),

          #  workspace movements
          'workspace up': Key('control:down, alt:down, up, control:up, alt:up'),
          'workspace down': Key('control:down, alt:down, down, control:up, alt:up'),
          'workspace left': Key('control:down, alt:down, left, control:up, alt:up'),
          'workspace right': Key('control:down, alt:down, right, control:up, alt:up'),

          # window workspace movements
          'twitch up': Key('control:down, alt:down, shift:down, up, control:up, alt:up, shift:up'),
          'twitch down': Key('control:down, alt:down, shift:down, down, control:up, alt:up, shift:up'),
          'twitch left': Key('control:down, alt:down, shift:down, left, control:up, alt:up, shift:up'),
          'twitch right': Key('control:down, alt:down, shift:down, right, control:up, alt:up, shift:up'),

          # open terminal
          'open terminal': Key('control:down, alt:down, t, control:up, alt:up'),
          'cancel': Key('c-c'),

          ##### letters
         # 'India':                             Key('i'),
         # 'quebec':                            Key('q'),
         # 'golf':                              Key('g'),
         'minus':                             Key('minus'),
        
        'alpha': Key('a'),
        'bravo': Key('b'),
        'charlie': Key('c'),
        'delta': Key('d'),
        'echo': Key('e'),
        'foxtrot': Key('f'),
        'golf': Key('g'),
        'hotel': Key('h'),
        'India|indigo': Key('i'),
        'juliet': Key('j'),
        'kilo': Key('k'),
        'lima': Key('l'),
        'mike': Key('m'),
        'november': Key('n'),
        'oscar': Key('o'),
        'papa|poppa': Key('p'),
        'quebec|quiche': Key('q'),
        'romeo': Key('r'),
        'sierra': Key('s'),
        'tango': Key('t'),
        'uniform': Key('u'),
        'victor': Key('v'),
        'whiskey': Key('w'),
        'x-ray': Key('x'),
        'yankee': Key('y'),
        'zulu': Key('z'),
        }

    # n 1-10 windows
    extras = [IntegerRef('n', 1, 10), Dictation('text')]
    defaults = {
        'n': 1,
        'text': ''
        }

    
grammar.add_rule(TestRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
