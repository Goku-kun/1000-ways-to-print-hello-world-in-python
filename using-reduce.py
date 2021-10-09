# Using reduce() function to reduce a list into a string and print it

from functools import reduce

helloworld = [ 'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!' ]

print(reduce(lambda a,b: a + b, helloworld))
