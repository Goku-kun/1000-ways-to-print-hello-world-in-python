# This script uses the files name '__file__' to print 'hello, world'
# FOR THIS SCRIPT TO WORK YOU MUST HAVE 'hello' AND 'world' SOMEWHERE IN IT'S FILE NAME!
hello = __file__.lower().find("hello")
world = __file__.lower().find("world")

print(f"{__file__[hello:hello+5]}, {__file__[world:world+5]}")
