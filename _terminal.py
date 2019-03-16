import aenea
from aenea import (
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    AppContext,
    ProxyAppContext,
    Text,
    Pause,
)


class MappingTerminal(MappingRule):
    mapping = {
        'open terminal': Key('control:down, alt:down, t, control:up, alt:up'),
        'cancel': Key('c-c'),
        # fzf
        'get command [<text>]': Key('c-r') + Pause('200') + Text('%(text)s'),
        'get file': Key('c-t'),
        'get folder': Key('a-c'),

        # copy/paste terminal
        'copy raw': Key('cs-c'),
        'plop raw': Key('cs-v'),
    }

    extras = [IntegerRef('n', 1, 10), Dictation('text')]
    defaults = {
        'n': 1,
        'text': ''
    }


chromium_context = aenea.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*terminal.*'),
    AppContext(title='chrome')
)
grammar = Grammar('terminal')
grammar.add_rule(MappingTerminal())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
