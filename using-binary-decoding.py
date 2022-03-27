import codecs
hex = [b"48", b"65", b"6c", b"6c", b"6f", b"20", b"57", b"6f", b"6c", b"64", b"0a"]
for i in hex:
    print(str(codecs.decode(i, "hex"), "utf-8"), end="")
