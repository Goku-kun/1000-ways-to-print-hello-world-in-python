#!/usr/bin/env python3

from re import finditer
from itertools import chain

target = "Hello, World!"
d = {tuple(i.start() for i in finditer(c, target)):c for c in set(target)}
print(''.join(chain(*[[d[key] for key in d if i in key] for i in range(len(target))])))
