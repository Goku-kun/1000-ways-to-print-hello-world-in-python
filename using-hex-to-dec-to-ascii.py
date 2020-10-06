hexlist = ['48','65','6C','6C','6F','2C','20','57','6F','72','6C','64','21']

res = ''
for c in hexlist:
    res+=chr(int(c, 16))

print(res)
