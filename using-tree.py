#!/usr/bin/env python3

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def str_to_tree(s):
    if len(s) == 0:
        return None
    ret = Tree(s[0])
    s = s[1:]
    l = len(s)
    ret.left = str_to_tree(s[:l//2])
    ret.right = str_to_tree(s[l//2:])
    return ret

def print_tree(t):
    if t == None:
        return
    print(t.data, end='')
    print_tree(t.left)
    print_tree(t.right)

print_tree(str_to_tree("Hello, World!\n"))