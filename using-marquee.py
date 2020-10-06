import sys
import time

def main():
    program = animate()
    program.data = input("Enter string : ") + " "
    program.width = int(input("Enter width : "))
    program.animate()


class animate:
    def __init__(self):
        self.data = ""
        self.width = 0

    def animate(self):
        try:
            while True:
                for x in range(0, self.width):
                    time.sleep(0.1)
                    msg = "\r{}{}".format(" " * x, self.data)
                    sys.stdout.write(msg)
                    sys.stdout.flush()

                for x in range(self.width, 0, -1):
                    time.sleep(0.1)
                    msg = "\r{}{}".format(" " * x, self.data)
                    sys.stdout.write(msg)
                    sys.stdout.flush()
        except KeyboardInterrupt:
            print("Exiting")


if __name__ == "__main__":
    main()