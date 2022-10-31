class Tree:

    def __init__(self, key) -> None:
        
        self.val = key
        self.left = None
        self.right = None

    def pre_order(self):
        print(self.val, end=' ')

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        
        if self.left:
            self.left.in_order()

        print(self.val, end=' ')

        if self.right:
            self.right.in_order()

    def post_order(self):
        
        if self.left:
            self.left.post_order()
        
        if self.right:
            self.right.post_order()
        
        print(self.val, end=' ')

# root = Tree(1)
# root.left = Tree(2)
# root.right = Tree(5)

# root.left.left = Tree(3)
# root.left.right = Tree(4)

# root.right.left = Tree(6)
# root.right.right = Tree(7)

# root.pre_order()
#1,2,3,4,5,6,7
# root.in_order()
# 3, 2, 4, 1, 6, 5, 7
#root.post_order()
# 3, 4, 2, 6, 7, 5, 1

root = Tree('D')
root.left = Tree('A')
root.right = Tree('V')

root.left.left = Tree('I')
root.left.right = Tree('B')

root.right.left = Tree('J')
root.right.right = Tree('U')

# In order
# I A B D J V U 

# pre order
# D A I B V J U

# post order
# I B A J U V D

