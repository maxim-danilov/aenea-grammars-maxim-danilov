from aenea import (
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    Text,
)


class MappingWindowManager(MappingRule):
    mapping = {
        # switcher
        'window': Key('a-space'),
        'window <windowNumber>': Key('c-f1:%(windowNumber)d'),

        # resize
        'window up': Key('control:down, win:down, up, control:up, win:up'),
        'window left': Key('control:down, win:down, left, control:up, win:up'),
        'window right': Key('control:down, win:down, right, control:up, win:up'),

        # workspaces
        'workspace up': Key('control:down, alt:down, up, control:up, alt:up'),
        'workspace down': Key('control:down, alt:down, down, control:up, alt:up'),
        'workspace left': Key('control:down, alt:down, left, control:up, alt:up'),
        'workspace right': Key('control:down, alt:down, right, control:up, alt:up'),

        # window workspace movements
        'twitch up': Key('control:down, alt:down, shift:down, up, control:up, alt:up, shift:up'),
        'twitch down': Key('control:down, alt:down, shift:down, down, control:up, alt:up, shift:up'),
        'twitch left': Key('control:down, alt:down, shift:down, left, control:up, alt:up, shift:up'),
        'twitch right': Key('control:down, alt:down, shift:down, right, control:up, alt:up, shift:up'),

        'fullscreen': Key('f11'),

        'stop time': Key('ca-lbracket'),
        'play time': Key('ca-rbracket'),

        # credentials
        'my e-mail': Text('danilov.ms.dev@gmail.com'),
    }

    extras = [IntegerRef('windowNumber', 1, 10), Dictation('text')]
    defaults = {
        'windowNumber': 1,
        'text': ''
    }


grammar = Grammar('window_manager')
grammar.add_rule(MappingWindowManager())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
