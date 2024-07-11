import threading
import time

# Morse code dictionary
morse_code = {
    'H': '....', 'E': '.', 'L': '.-..', 'O': '---',
    ',': '--..--', ' ': ' ', 'W': '.--', 'R': '.-.',
    'D': '-..', '!': '-.-.--'
}

# Conversion of text to Morse code
def to_morse(text):
    return ' '.join(morse_code[c] for c in text)

# Function to blink Morse code using threading
def blink_morse(morse):
    for symbol in morse:
        if symbol == '.':
            print('•', end='', flush=True)
            time.sleep(0.2)
        elif symbol == '-':
            print('—', end='', flush=True)
            time.sleep(0.6)
        else:
            time.sleep(0.4)
        time.sleep(0.2)

# "Hello, World!" to Morse code
message = to_morse("HELLO, WORLD!")

# Create and start a thread to blink Morse code
thread = threading.Thread(target=blink_morse, args=(message,))
thread.start()

thread.join()

# Print the final message
print("\nHello, World!")

