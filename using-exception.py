#Hello World Program using exceptions

try:
   raise Exception("Hello, World!")
except Exception as e:
   print(e.args[0])      