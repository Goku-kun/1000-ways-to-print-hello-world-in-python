# Hello World (plain and cipher text) using Caesar Cipher
def caesar(text, shift):
	result = ""
	for char in text:
		if char.isupper():
			result += chr((ord(char) + shift - 65) % 26 + 65)		# caesar uppercase characters
		else:
			result += chr((ord(char) + shift - 97) % 26 + 97)		# caesar lowercase characters
	return result

text = "HelloWorld"
shift = 4															# Shift by bits
print("Plain Text :", text)
print("Shift :", shift)
print("Cipher Text: ", caesar(text,shift))
