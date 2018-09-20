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


class ChromiumRule(MappingRule):
    mapping = aenea.configuration.make_grammar_commands('chromium', {
        'open frame': Key('c-t'),
        'close frame [<n>]': Key('c-w:%(n)d'),
        'frame [<n>]': Key('c-%(n)d'),
        'frame left [<n>]': Key('cs-tab:%(n)d'),
        'frame right [<n>]': Key('c-tab:%(n)d'),

        # url
        'search [<text>]': Key('c-k') + Text('%(text)s'),
        'address': Key('c-l'),

        # find
        'voice search': Key('c-backslash'),
        'find [<text>]': Key('c-f') + Text('%(text)s'),
        'next [<n>]': Key('c-g:%(n)d'),
        'previous [<n>]': Key('cs-g:%(n)d'),

        'history': Key('c-h'),
        'bookmarks': Key('c-h'),

        # navigation
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
        'slide': Text('}'),
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
