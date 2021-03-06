import time

from dragonfly import Function
from natlink import setMicState

import aenea.configuration
from aenea import (
    AppContext,
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    ProxyAppContext,
    Text,
    Pause,
    Repeat,
)


def mute_microphone():
    setMicState("off")
    time.sleep(11)
    setMicState('on')

class ChromiumRule(MappingRule):
    mapping = aenea.configuration.make_grammar_commands('chromium', {
        'open frame': Key('c-t'),
        'close frame [<n>]': (Key('c-w') + Pause('40')) * Repeat(extra='n'),
        'frame [<n>]': Key('c-%(n)d'),
        'west [<n>]': Key('cs-tab:%(n)d'),
        'east [<n>]': Key('c-tab:%(n)d'),

        # url
        'search [<text>]': Key('c-k') + Text('%(text)s'),
        'address': Key('c-l'),

        # search query
        # 'selection': Key('c-c') + Key('c-t') + Pause('90') + Key('c-v') + Key('enter'),
        'quick search': Key('c-t') + Key('c-v') + Key('enter'),
        'voice search': Key('c-1') + Function(mute_microphone),

        # find on a page
        'find [<text>]': Key('c-f') + Text('%(text)s'),
        'bind [<text>]': Text('/') + Pause('50') + Text('%(text)s'),
        'next [<n>]': Key('c-g:%(n)d'),
        'previous [<n>]': Key('cs-g:%(n)d'),

        'history': Key('c-h'),
        'bookmarks': Key('c-h'),

        # navigation
        'back [<n>]': Key('a-left:%(n)d'),
        'reload': Key('c-r'),

        # 'back [<n>]':                      Key('a-left:%(n)d'), -> to global
        'forward [<n>]': Key('a-right:%(n)d'),

        # vimium
        'link': Key('f'),
        'new link': Key('s-f'),
        'number [<n>]': Text('%(n)d'),

        # zoom
        'zoom in [<n>]': Key('c-plus:%(n)d'),
        'zoom out [<n>]': Key('c-minus:%(n)d'),

        # scroll slow
        'slide': Key('c-0'),
    })

    extras = [IntegerRef('n', 1, 100), Dictation('text')]
    defaults = {
        'n': 1,
        'text': ''
    }


chromium_context = aenea.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*chrome.*'),
    AppContext(title='chrome')
)
chromium_grammar = Grammar('chromium', context=chromium_context)
chromium_grammar.add_rule(ChromiumRule())
chromium_grammar.load()


def unload():
    global chromium_grammar
    if chromium_grammar:
        chromium_grammar.unload()
    chromium_grammar = None
