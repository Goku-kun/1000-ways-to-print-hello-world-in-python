import random
alpha = ["H" , "L" , "L" ,"E" ,"O"]
beta = ["W" , "R", "L" , "D", "O"]
random.shuffle(alpha)
random.shuffle(beta)
while ("".join(alpha) + " " + "".join(beta)) != "HELLO WORLD":
    random.shuffle(alpha)
    random.shuffle(beta)

print("".join(alpha) + " " + "".join(beta))
