#! /usr/bin/python3

string = ""

from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def addChar(symbol):
    global string
    for i in range(31,128):
        print(string + chr(i))
        clear()
        if chr(i) == symbol:
            string += symbol
            return


addChar('H')
addChar('e')
addChar('l')
addChar('l')
addChar('o')
addChar(' ')
addChar('w')
addChar('o')
addChar('r')
addChar('l')
addChar('d')
addChar('!')

print(string)
