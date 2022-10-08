from dataclasses import dataclass
from re import M

@dataclass
class Stack:

    items = []

    def push(self, item):
        self.items.append(item)
    
    def top(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()
    
    def bottom(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


my_custom_stack = Stack()

my_custom_stack.push(1)
my_custom_stack.push(2)
my_custom_stack.push(3)
my_custom_stack.push('Ho')
my_custom_stack.push('la')



# print(my_custom_stack.top())
# print(my_custom_stack.top())
# print(my_custom_stack.top())

while not my_custom_stack.is_empty():
    print(my_custom_stack.pop())
