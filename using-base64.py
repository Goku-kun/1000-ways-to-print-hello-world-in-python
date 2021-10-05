from base64 import b64decode
encoded_hello_world = 'SGVsbG8sIFdvcmxkIQ=='.encode('utf8')
decoded_hello_world = b64decode(encoded_hello_world).decode('utf8')
print(decoded_hello_world)
