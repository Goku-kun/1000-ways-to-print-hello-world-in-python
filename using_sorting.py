#uses sorting with the help of dictionary
import random
dict = {
    1: "H",
    2: "E",
    3: "L",
    4: "L",
    5: "O",
    6: " ",
    7: "W",
    8: "O",
    9: "R",
    10: "L",
    11: "D",
}

#scrambling a random order, could also take user input
alpha = ["" for x in range (11)]
for i in range(1,12):
    a = random.randint(0,10)
    while alpha[a] != "":
        a = random.randint(0,10)
    alpha[a] = i

#now I have a scrambled order with numbers mapped to alphabets using dictionary, we sort this now

alpha.sort()
for i in alpha:
    print(dict[i], end = "")
