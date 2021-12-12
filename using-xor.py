#!/usr/bin/env python3

ct = b'\x3d\x0b\x0d\x1f\x1c\x59\x4d\x3e\x01\x15\x07\x01\x58'
key = b'unassumingkey'

print(''.join(chr(ct[i]^key[i]) for i in range(13)))