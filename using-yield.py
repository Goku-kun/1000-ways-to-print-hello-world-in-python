# Print Hello, World using yield generator

def createYield():
  yield "Hello, World!"

generator = createYield()
for i in generator:
  print(i)