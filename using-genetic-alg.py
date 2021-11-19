#!/usr/bin/env python3

from random import randint, choice, random

target = b"Hello, World!"
verbose = 1
mutation_factor = 5

def fitness(x): #larger val is less fit
    return sum(abs(x[i]-target[i]) for i in range(len(target)))

def init_child():
    return bytes(randint(32, 126) for _ in range(len(target)))

def clip(x):
    return min(max(x, 32), 126)

def make_child(a, b):
    return bytes(clip((a[i]+b[i])//2 + randint(-mutation_factor, mutation_factor))
                     for i in range(len(a)))

def reproduce(ents):
    out = [i for i in ents]
    for ent in ents:
        out.append(make_child(ent, choice(ents)))
    return out

def cull(ents): # assumes sorted by fitness, best entities first
    out = []
    for i, ent in enumerate(ents):
        if random() > ((i+1)/len(ents)):
            out.append(ent)
    return out

if __name__ == '__main__':
    ents = [init_child() for i in range(10000)]
    for gen in range(10000):
        ents = sorted(ents, key=lambda x:fitness(x))
        ents = cull(ents)
        if (gen+1)%100 == 0:
            print(f"Best 5 of Gen {gen+1}: {ents[:5]}")
            print(len(ents))
        ents = reproduce(ents)
