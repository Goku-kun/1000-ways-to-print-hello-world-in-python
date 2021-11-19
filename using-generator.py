#!/usr/bin/env python3

def gen():
    target = "Hello, World!"
    while len(target) > 0:
        yield target[0]
        target = target[1:]

print(''.join(gen()))