try:
  raise Exception("Hello, World!")
except Exception as e:
  print(str(e))