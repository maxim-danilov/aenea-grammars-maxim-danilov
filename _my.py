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
        'window': Key('a-space'),
        'window <windowNumber>': Key('c-f1:%(windowNumber)d'),

        'fullscreen': Key('f11'),

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
        'whack [<n>]': Key('c-w:%(n)d'), # todo: create separated contexts for the terminal
    }

    extras = [IntegerRef('windowNumber', 1, 10), IntegerRef('n', 1, 100), Dictation('text')]
    defaults = {
        'windowNumber': 1,
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
