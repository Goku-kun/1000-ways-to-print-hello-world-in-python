import sys

output = []

inputdict = {
    str(['h', 1]) : 1,
    str(['e', 1]) : 1,
    str(['l', 1]) : 2,
    str(['o', 1]) : 1,
    str([' ', 1]) : 1,
    str(['w', 1]) : 1,
    str(['o', 2]) : 1,
    str(['r', 1]) : 1,
    str(['l', 2]) : 1,
    str(['d', 1]) : 1,

}

for k,v in inputdict.items():
    sys.stdout.write((list(k))[2]*v)
