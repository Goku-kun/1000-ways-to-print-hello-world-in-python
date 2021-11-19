#!/usr/bin/env python3

class Tree:
    def __init__(self, data):
        if len(data) == 0:
            self.data = None
            self.right = None
            self.left = None
            return
        self.data = data[0]
        data = data[1:]
        l = len(data)
        self.left = Tree(data[:l//2])
        self.right = Tree(data[l//2:])

def print_tree(t):
    if t.data == None:
        return
    print(t.data, end='')
    print_tree(t.left)
    print_tree(t.right)

print_tree(Tree("Hello, World!\n"))