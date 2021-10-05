class MorseCodeCipher:
    def __init__(self):
        """ This is a python implementation of Roman Numeral Cipher"""

        self.morse_dict = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ',': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'
                           }

        self.reverse_morse = {self.morse_dict[key]: key for key in self.morse_dict}

    def encrypt(self, text: str) -> str:
        result = ''

        for ch in text.upper():
            if ch != ' ':
                val = self.morse_dict.get(ch, ch)
                result += (val + ' ')
            else:
                result += ' '

        return result

    def decrypt(self, text: str) -> str:
        text = text.strip(' ') + ' '
        result = ''

        i = 0
        char = ''
        space_ct = 0

        while i < len(text):
            if text[i] == ' ':
                if space_ct == 0:
                    result += self.reverse_morse.get(char, char)
                    space_ct += 1
                    char = ''
                else:
                    space_ct += 1
            else:
                if space_ct > 0:
                    result += ' ' * (space_ct - 1)
                    space_ct = 0
                char += text[i]

            i += 1

        return result

if __name__ == '__main__':
    cipher = MorseCodeCipher()
    message = 'Hello world 😊'

    encrypted = cipher.encrypt(message)
    decrypted = cipher.decrypt(encrypted)

    print(encrypted)
    print(decrypted)
