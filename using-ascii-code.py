s = ""
ascii = [72,101,108,108,111,44,32,87,111,114,108,100,33]

for i in ascii:
  s = s + chr(i)

print(s)

# going from string version to an ascii version
helloworld = 'hello world'

for letter in helloworld:
    print(ord(letter), '-', chr(ord(letter)) )

