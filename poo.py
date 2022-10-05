from dataclasses import dataclass
from abc import ABC, abstractclassmethod
from turtle import st

class Person(ABC):

    def __init__(self, name, age) -> None:
        
        self.name = name
        self.age = age

    @abstractclassmethod
    def say_hello(self):
        pass

    @abstractclassmethod
    def say_goodbye(self):
        raise NotImplementedError("Buddy please implement this method")
    
    def __str__(self) -> str:
        return f"{self.name} {self.age}"



class Student(Person):

    def __init__(self, name, age, school) -> None:
        super().__init__(name, age)
        self.school = school
        self.__is_enabled = True
    
    def say_hello(self):
        return f'Hi from {self.name}'
    
    def say_goodbye(self):
        return f'goodbye from {self.name}'
    
    def __str__(self) -> str:
        return super().__str__() + f" and i am student at {self.school}"

    def enabled(self):
        self.__is_enabled = True
    
    def disable(self):
        self.__is_enabled = False
    
    def get_enabled(self):
        return self.__is_enabled

student = Student('Jorge', 30, 'Academlo')
print(student)
student.disable()
print(student.get_enabled())