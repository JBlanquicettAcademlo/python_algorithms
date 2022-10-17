from dataclasses import dataclass

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
    
    def sorted_insert(self, key):

        if not self.items or key > self.items[-1]:
            self.items.append(key)
            return
        
        top = self.items.pop()

        self.sorted_insert(key)
        self.items.append(top)


    def sort_stack(self):

        if not self.items:
            return
        
        top = self.items.pop()
        self.sort_stack()
        self.sorted_insert(top)


my_custom_stack = Stack()

my_custom_stack.push(5)
my_custom_stack.push(-2)
my_custom_stack.push(9)
my_custom_stack.push(7)
my_custom_stack.push(3)

print(my_custom_stack.items)
my_custom_stack.sort_stack()
print(my_custom_stack.items)

# 3 -> [-2, 5, 7, 9] -> [-2, 5, 7] -> [-2, 5] -> [-2, 3] -> [-2, 3, 5] -> [-2, 3, 5, 7] 
# .. -> [-2, 3, 5, 7, 9]

# 7 -> [-2, 5, 9] -> [-2, 5] -> [-2, 5, 7, 9]
# 9 -> [-2, 5] -> [-2, 5, 9]
# -2 -> [5] -> [] -> [-2, 5]
# 5 -> [] -> [5]
