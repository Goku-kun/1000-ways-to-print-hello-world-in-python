import sys



inputdict = {
    str(['H', 1]) : 1, #the list in the key has 2 elements, first one corresponds to the character and the second one corresponds to the nth occurence of the character
    str(['e', 1]) : 1,  #the value of the dict elements corresponds to the number of times the respective character repeats itself at a particular point in the world
    str(['l', 1]) : 2,
    str(['o', 1]) : 1,
    str([' ', 1]) : 1,
    str(['W', 1]) : 1,
    str(['o', 2]) : 1,
    str(['r', 1]) : 1,
    str(['l', 2]) : 1,
    str(['d', 1]) : 1,
    str(['!', 1]) : 1,

}

for k,v in inputdict.items():          #iterated over the list and printed the character times the number of times it occurs after converting the string key back to a list
    sys.stdout.write((list(k))[2]*v)
