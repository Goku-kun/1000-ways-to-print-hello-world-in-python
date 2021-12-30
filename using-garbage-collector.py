#!/usr/bin/env python3

import gc

for obj in gc.get_objects():
    if (obj == print):
        obj("Hello, World!")
        break
