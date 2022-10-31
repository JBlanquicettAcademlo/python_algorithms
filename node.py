

class Node(object):

    def __init__(self, data, next=None) -> None:
        
        self.__data = data
        self.__next = next

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data


    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next
    
    def __str__(self) -> str:
        return 'Node ['+str(self.__data)+']'

node1 = Node('Manzana')
node2 = Node('Pera', node1)
node3 = Node('Uva', node2)

while node3:
    print(node3.get_data())
    node3 = node3.get_next()