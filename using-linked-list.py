class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head_node = None

    def add_node(self, value):
        if self.head_node:
            new_node = Node(value, self.head_node)
            self.head_node = new_node
        else:
            self.head_node = Node(value)

    def values_as_list(self):
        lst = []
        current_node = self.head_node
        while current_node:
            lst.append(current_node.value)
            current_node = current_node.next_node
        return lst

x = LinkedList()
for char in "Hello, World!":
    x.add_node(char)

y = x.values_as_list()
y.reverse()
print("".join(y))