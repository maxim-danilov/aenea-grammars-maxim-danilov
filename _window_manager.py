import json
import time

from dragonfly import Function
from natlink import setMicState

from aenea import (
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    Text,
)

private_data = json.loads(open('C:\private-data.json').read())

def mute_microphone():
    setMicState("off")
    time.sleep(5)
    setMicState('on')

class MappingWindowManager(MappingRule):
    mapping = {
        # switcher
        'window': Key('a-space'),
        'window <windowNumber>': Key('c-f1:%(windowNumber)d'),
        'my feature': Key('a-space') + Key('up') + Key('enter'),

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

        # upwork timer
        'stop time': Key('ca-lbracket'),
        'play time': Key('ca-rbracket'),

        # search for Google
        'look up': Key('ca-lbracket') + Key('c-4'),
        # 'google': Key('c-4'),


        # call my tts script
        'speech': Key('c-lbracket'),

        # credentials
        'my name': Text('Maxim'),
        'my lastname': Text('Danilov'),
        'my e-mail one': Text('700ghz@gmail.com'),
        'my e-mail two': Text('danilov.ms.dev@gmail.com'),
        'private long': Text(private_data[0]),
        'private short': Text(private_data[1]),
        'private system': Text(private_data[2]),

        'close this window': Key('a-f4'),

        # my launcher
        'my launcher': Key('a-dot'),

        # system macros
        'record actions': Key('c-9'),
        'play actions': Key('c-0'),

        # call my Google voice recognition script
        'say russian': Key('a-comma') + Function(mute_microphone),
        # 'say english': Key('a-dot'),
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
