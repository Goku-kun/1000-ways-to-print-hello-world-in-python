from multiprocessing import Pool
import os
import time

def heavy_print(x):
    return x

if __name__ == '__main__':
    with Pool(os.cpu_count()) as p:
        text = list("Hello World")
        print(''.join(p.map(heavy_print, text)))
