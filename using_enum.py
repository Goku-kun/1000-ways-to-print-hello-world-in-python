from enum import Enum, auto


class Message(Enum):
    HELLO = auto()
    WORLD = auto()

    def __str__(self):
        return self.name.capitalize()


print(f"{Message.HELLO}, {Message.WORLD}!")
