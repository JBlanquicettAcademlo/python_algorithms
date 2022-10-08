from dataclasses import dataclass

@dataclass
class AcademloList:

    __l:list

    def __init__(self) -> None:

        self.__l = []
    
    def get_size(self):
        return len(self.__l)
    
    def is_empty(self):
        return len(self.__l)==0

    def head(self):
        if self.is_empty():
            raise Exception('AcademloList have not items')
        return self.__l[0]
    
    def add(self, e):
        self.__l.append(e)
    
    def get(self, index):
        if self.is_empty():
            raise Exception('AcademloList have not items')
        try:
            return self.__l[index]
        except IndexError as i:
            print(f'AcademloList {i}')
            return -1



academlo_list = AcademloList()

print(academlo_list.is_empty())
print(academlo_list.get_size())
# print(academlo_list.head())

academlo_list.add("H")
academlo_list.add("o")
academlo_list.add("l")
academlo_list.add("a")

print(academlo_list.is_empty())
print(academlo_list.get_size())
print(academlo_list.get(2))

print(academlo_list.get(1000))
