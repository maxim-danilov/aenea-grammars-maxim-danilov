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


class WebstormRule(MappingRule):
    mapping = aenea.configuration.make_grammar_commands('webstorm', {
        'explore': Key('a-1'),
        'hide': Key('s-escape'),

        # git
        'grey': Key('a-9'),
        'commit': Key('c-k'),
        'push': Key('cs-k'),
        'next diff': Key('f7'),
        'preev diff': Key('s-f7'),
        'revert': Key('ca-z'),
        'difference': Key('c-d'),

        # frames
        'touch [<n>]': Key('c-tab:%(n)d'),

        # search
        'fuzz [<text>]': Key('cs-n') + Pause('100') + Text('%(text)s'),
        'search': Key('cs-f'),
        'search all': Key('a-1') + Pause('200') + Key('home') + Key('cs-f'),
        'quick search': Key('a-1') + Pause('100') + Key('home') + Pause('100') + Key('cs-f') + Pause('100') + Key('c-v'),
        'tidy up': Key('cs-a') + Pause('100') + Text('fix eslint') + Pause('100') + Key('enter'),

        # declaration/using
        'more': Key('g,d'),
        'check': Key('c-f7'),
        'check detail': Key('c-f7'),

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
        'copy name': Key('c-7'),
        'copy object': Key('c-8'),
        'evaluate': Key('a-f8') + Pause('100') + Key('a-v') + Pause('100') + Key('a-r'),

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
        'west frame [<n>]': (Key('a-left') + Pause('40')) * Repeat(extra='n'),
        'east frame [<n>]': (Key('a-right') + Pause('40')) * Repeat(extra='n'),
        'close frame [<n>]': (Key('c-f4') + Pause('40')) * Repeat(extra='n'),

        # vsplit switch
        'file left': Key('c-w, h'),
        'file right': Key('c-w, l'),

        'terminal': Key('a-f12'),
        'motion': Key('c-3'),
        
        # scratch file
        'scratch file': Key('cas-insert'),

        ###
        'set wrap': Key('cs-a') + Text('acwr') + Pause('100') + Key('enter') + Key('escape'),

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
