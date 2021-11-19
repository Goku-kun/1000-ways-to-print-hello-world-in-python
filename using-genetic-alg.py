#!/usr/bin/env python3

from random import randint, choice, random, gauss

target = b"Hello, World!"
verbose = 0
mut_factor = 1

def fitness(x): #larger val is less fit
    return sum(abs(x[i]-target[i])**2 for i in range(len(target)))

def init_child():
    return bytes(randint(32, 126) for _ in range(len(target)))

def clip(x):
    return min(max(x, 32), 126)

def make_child(a, b):
    return bytes(clip((a[i]+b[i])//2 + int(gauss(0, mut_factor)))
                     for i in range(len(a)))

def reproduce(ents):
    out = [i for i in ents]
    for ent in ents:
        out.append(make_child(ent, choice(ents)))
    return out

def cull(ents): # assumes sorted by fitness, best entities first
    out = []
    for i, ent in enumerate(ents):
        if random() > (i/len(ents)):
            out.append(ent)
    return out[:init_val//2]

if __name__ == '__main__':
    init_val = 100
    ents = [init_child() for i in range(init_val)]
    gen = 0
    while True:
        ents = sorted(ents, key=lambda x:fitness(x))
        if ents[0] == target:
            print(ents[0].decode())
            if verbose:
                print(f"Solved after {gen} generations.")
            exit()
        ents = cull(ents)
        if verbose and (gen+1)%100 == 0:
            print(f"Best 5 of Gen {gen+1}: {ents[:5]}")
            print(len(ents))
        ents = reproduce(ents)
        gen += 1
