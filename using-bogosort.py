#!/usr/bin/env python3

from random import shuffle

target = list("Hello, World!")

while True:
    shuffle(target)
    if target == list("Hello, World!"):
        print(''.join(target))
        exit()
