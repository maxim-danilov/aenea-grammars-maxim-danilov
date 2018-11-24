import aenea
from aenea import (
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    AppContext,
    ProxyAppContext,
)


class MappingTerminal(MappingRule):
    mapping = {
        'open terminal': Key('control:down, alt:down, t, control:up, alt:up'),
        'cancel': Key('c-c'),
        # fzf
        'get command': Key('c-r'),
        'get file': Key('c-t'),
        'get folder': Key('a-c'),
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
