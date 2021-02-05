# Add each character of a (reversed) string to a stack, pop characters off stack into a list, and print joined list

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, value):
        node = Node(value)
        node.next_node = self.top
        self.top = node
        self.size += 1
    def pop(self):
        if self.size != 0:
            node_to_pop = self.top
            self.top = node_to_pop.next_node
            self.size -= 1
            return node_to_pop.value

text = "!dlrow ,olleH"

stack = Stack()

for i in range(len(text)):
    stack.push(text[i])

result = []

while stack.size > 0:
    result.append(stack.pop())

print("".join(result))