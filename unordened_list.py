from dataclasses import dataclass

@dataclass
class UnordenedList:

    items = []

    def add(self, e):
        self.items.insert(len(self.items), e)
    
    def get_all(self):
        return self.items

u = UnordenedList()

u.add(1)
u.add(2)
u.add(7)
u.add(3)
u.add(-4)

print(u.get_all())