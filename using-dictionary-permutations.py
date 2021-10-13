from itertools import permutations
from sys import stdout, argv

reference = {100: 'd', 101: 'e', 104: 'h', 108: 'l', 111: 'o', 114: 'r', 119: 'w'}
vowels = ['e', 'o']
words = [
    {'len': 5, 'first': 104, 'last': 111, 'repeat': True, 'r_char': 108},
    {'len': 5, 'first': 119, 'last': 100, 'repeat': False, 'r_char': None}
]
second_last = 108


def find_words(repeat, r_char):
    output = []
    chars = [y for x, y in reference.items()]
    if repeat:
        chars.append(reference[r_char])
    for value in range(0, len(chars)):
        output += [x for x in permutations(chars[value:])]
    return output


def filter_word(value, first, last, repeat, r_char):
    output = False
    value = [x for x in value]
    first_char, second_char, second_last_char, last_char = value[0], value[1], value[-2], value[-1]
    if first_char == first and last_char == last and second_char != last_char and ord(second_last_char) == second_last:
        if second_char in vowels and second_char in [y for x, y in reference.items()]:
            string = []
            last = None
            for char in value:
                if last != None:
                    if char == last and char not in vowels:
                        string.append(char)
                    elif char != last:
                        string.append(char)
                else:
                    string.append(char)
                last = char
            if len(string) == len(value):
                if repeat:
                    last = None
                    for char in value:
                        if last != None:
                            if char == last:
                                output = True
                        last = char
                else:
                    third_char = value[2]
                    if ord(third_char) > ord(second_last_char) and ord(second_char) > ord(second_last_char):
                        output = True
    return output


def find_word(values, first, last, length, repeat, r_char):
    first, last, output, items, count = reference[first], reference[last], [], [], 0
    if repeat:
        r_char = reference[r_char]
    for value in values:
        count += 1
        for item in [x[:length] for x in permutations(value)]:
            item = ''.join(item)
            if item not in items and filter_word(value=item, first=first, last=last, r_char=r_char, repeat=repeat):
                items.append(item)
        if debug:
            count_out = '(%s/%s) (%s%%) (%s found)' % (
            count, len(values), (round(100 * float(count) / float(len(values)), 2)), len(items))
            stdout.write('%s%s' % (('\r' * len(count_out)), count_out))
            stdout.flush()
        if len(items) >= 1 and aggressive:
            break
    for item in items:
        output.append(item)
    return output


if __name__ == '__main__':
    debug = 'debug' in argv
    aggressive = 'aggressive' not in argv
    if debug:
        print('Building string...')
    data = []
    for word in words:
        repeat = word['repeat']
        r_char = word['r_char']
        length = word['len']
        first_letter = word['first']
        last_letter = word['last']
        possible = find_words(repeat=repeat, r_char=r_char)
        data.append(
            find_word(values=possible, first=first_letter, last=last_letter, length=5, repeat=repeat, r_char=r_char))
    print(' '.join(x[0] for x in data))
