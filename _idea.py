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
        'next diff': Key('f7'),
        'preev diff': Key('s-f7'),
        'revert': Key('ca-z'),
        'difference': Key('c-d'),

        # frames
        'touch [<n>]': Key('c-tab:%(n)d'),

        # search
        'fuzz [<text>]': Key('cs-n') + Text('%(text)s'),
        'search': Key('cs-f'),
        'search all': Key('a-1') + Pause('200') + Key('home') + Key('cs-f'),
        'tidy up': Key('cs-a') + Text('fix eslint') + Pause('100') + Key('enter'),

        # declaration/using
        'more': Key('g,d'),
        'check': Key('ca-7'),
        'check detail': Key('a-f6'),

        # comment line
        'disable [<n>]': Key('c-slash:%(n)d'),

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
        'add watch': Key('c-6'),
        'copy watch': Key('c-7'),

        # code-folding
        'expand': Key('c-equal'),
        'expand all': Key('cs-plus'),
        'collapse': Key('c-minus'),
        'collapse all': Key('cs-minus'),

        # comments
        'comment [<text>]': Text('o// %(text)s'),

        # snippets
        'insert': Key('c-j'),

        # string manipulation
        'switch case': Key('as-m'),

        # frames
        'west [<n>]': Key('a-left:%(n)d'),
        'east [<n>]': Key('a-right:%(n)d'),

        # vsplit switch
        'file left': Key('c-w, h'),
        'file right': Key('c-w, l'),

        # copy to register a
        'start append copy': Text('"ay'),
        'append copy': Text('"Ay'),

        'terminal': Key('a-f12'),

    })

    extras = [IntegerRef('n', 1, 100), Dictation('text'), IntegerRef('line_number', 1, 9999)]
    defaults = {
        'n': 1,
        'text': '',
    }

webstorm_context = aenea.AeneaContext(
    ProxyAppContext(match='regex', title='.*(webstorm|pycharm).*'),
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
