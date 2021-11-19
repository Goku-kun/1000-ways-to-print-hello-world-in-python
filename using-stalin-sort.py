#!/usr/bin/env python3

from random import choice

target = "Hello, World!"

def gen():
    letters = list(set(target))
    while True:
        yield(choice(letters))

init_list = [next(gen()) for i in range(1000)]

idx = 0
while len(target) > 0:
    if init_list[idx] == target[0]:
        target = target[1:]
        idx += 1
    else:
        init_list.pop(idx)

print(''.join(init_list[:idx]))