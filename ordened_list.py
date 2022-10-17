from dataclasses import dataclass
from bubble_sort import bubble_sort

@dataclass
class OrdenedList:

    items = []

    def add(self, e):
        self.items.insert(len(self.items), e)
    
    def get_all(self):
        return bubble_sort(self.items)

u = OrdenedList()

u.add(1)
u.add(2)
u.add(7)
u.add(3)
u.add(-4)

print(u.get_all())