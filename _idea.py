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
)


class WebstormRule(MappingRule):
    mapping = aenea.configuration.make_grammar_commands('webstorm', {
        'explore': Key('a-1'),
        'hide': Key('s-escape'),

        # git
        'git': Key('a-9'),
        'commit': Key('c-k'),
        'push': Key('cs-k'),
        'next change': Key('f7'),
        'prev change': Key('s-f7'),

        # frames
        'touch [<n>]': Key('c-tab:%(n)d'),

        # search
        'fuzz [<text>]': Key('cs-n') + Text('%(text)s'),
        'search [<text>]': Key('cs-f') + Text('%(text)s'),
        'quick search': Key('a-1') + Key('home') + Key('cs-f') + Key('c-v'),
        'tidy up': Key('cs-a') + Text('fix eslint') + Pause('100') + Key('enter'),


        # declaration/using
        'more': Key('g,d'),
        'check': Key('ca-7'),
        'check detail': Key('a-f7'),

        # comment line
        'disable [<n>]': Key('c-slash:%(n)d'),

        # vim
        'line': Text('gg'), # say one two three line
        'find <text>': Text('/\c%(text)s'),

        'record macro': Text('qq'),
        'play macro': Text('@q'),
        'play macro two': Text('@w'),

        'remove line': Text('dd'),

        'mark that': Text('ma'),
        'jump mark': Text(''''a'''),

        'inside string': Text('@u'),
        'inside bracket': Text('@y'),

        # refactor
        'improve': Key('csa-t'),
        'rename': Key('s-f6'),

        # debugger
        'debug': Key('a-5'),
        'again': Key('c-f2') + Key('c-f5'),
        'stop': Key('c-f2'),
        'continue': Key('f9'),
        'next': Key('f8'),
        'step into': Key('f7'),
        'breakpoint': Key('c-f8'),
        'all breakpoints': Key('cs-f8') + Key('cs-f8') + Pause('80') + Key('cs-f8') + Key('cs-f8'),
        'run here': Key('a-f9'),
         
        # code-folding
        'expand': Key('c-equal'),
        'expand all': Key('cs-plus'),
        'collapse': Key('c-minus'),
        'collapse all': Key('cs-minus'),

        # comments
        'comment [<text>]': Text('o// %(text)s'),

        # snippets
        'insert': Key('c-j'),

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
