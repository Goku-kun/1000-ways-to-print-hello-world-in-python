class Printer:
      def __init__(self):
            super().__init__()
            self.var = "Hello, World!"
      def display(self):
            return self.var
print(Printer().display())
