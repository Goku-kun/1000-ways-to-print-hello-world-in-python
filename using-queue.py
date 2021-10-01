# Add each character of a string to a queue, pop characters off queue into a list, and print joined list

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        node = Node(value)
        if self.front is not None:
            temp = self.front
            while temp.next_node is not None:
                temp = temp.next_node
            temp.next_node = node
        else:
            self.front = node

    def pop(self):
        if self.front is not None:
            node_to_pop = self.front
            self.front = node_to_pop.next_node
            return node_to_pop.value
        raise IndexError("Queue Empty")

queue = Queue()

for i in "Hello, world!":
    queue.push(i)

result = []

while queue.front is not None:
    result.append(queue.pop())

print("".join(result))