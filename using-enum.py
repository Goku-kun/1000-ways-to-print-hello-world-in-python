#Printing Hello World using Enums
import enum
class Message(enum.Enum):
    Hello_World = "Hello, World!"

print(Message.Hello_World.value)    