from dataclasses import dataclass

@dataclass
class Animal: 

    __id:int
    name:str
    age:int
    color: str

    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.color}'

    
class Auto: 

    def __init__(self, id, color, model, brand) -> None:
        
        self.__id = id
        self.color = color
        self.model = model
        self.brand = brand

    def __str__(self) -> str:
        return f'{self.color} {self.model} {self.brand}'

auto = Auto(1, 'Blue', '1999', 'Ford')
print(auto)

animal = Animal(1, 'Dog', 50, 'White')
print(animal)

