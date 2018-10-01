import aenea.configuration

from aenea import (
    AppContext,
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    ProxyAppContext,
    Text
)


class WebstormRule(MappingRule):
    mapping = aenea.configuration.make_grammar_commands('webstorm', {
        'explore': Key('a-1'),
        'hide': Key('s-escape'),

        'git': Key('a-9'),
        'commit': Key('c-k'),
        'push': Key('cs-k'),
        'next git diff': Key('f7'),
        'prev git diff': Key('s-f7'),

        'touch [<n>]': Key('c-tab:%(n)d'),

        'fuzz': Key('cs-n'),

        'more': Key('g,d'),
        'check': Key('ca-7'),

        'disable [<n>]': Key('c-slash:%(n)d'),

        # vim
        'line <line_number>': Text('%(line_number)dgg'),
        'find <text>': Text('/\c%(text)s'),
    })

    extras = [IntegerRef('n', 1, 100), Dictation('text'), IntegerRef('line_number', 1, 9999)]
    defaults = {
        'n': 1,
        'text': '',
    }

webstorm_context = aenea.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*webstorm.*'),
    AppContext(title='webstorm')
)
webstorm_grammar = Grammar('chromium', context=webstorm_context)
webstorm_grammar.add_rule(WebstormRule())
webstorm_grammar.load()


def unload():
    global webstorm_grammar
    if webstorm_grammar:
        webstorm_grammar.unload()
    webstorm_grammar = None
