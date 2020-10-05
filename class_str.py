# printing hello world using magic method __str__ for a class

class Printer:
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return self.text
      
hello_world = Printer("Hello, world!")
print(hello_world)
