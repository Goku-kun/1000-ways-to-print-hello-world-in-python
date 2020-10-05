# this is probably one of the worst ways possible
# this script might actually be interesting for statistical purposes on the random() function. who knows.

import random

target = "Hello world!"
strlen = len(target)
i = 0
while i != strlen:
  cascii = random.randint(0,127)
  if chr(cascii) == target[i]:
    print(chr(cascii), end="")
    i += 1
print("")
