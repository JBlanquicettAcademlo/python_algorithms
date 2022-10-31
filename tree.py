

# value1 ={'value':1, 'children':[]}
# value4 ={'value':4, 'children':[]}

# left ={'value':5, 'children':[value1, value4]}

# center ={'value':9, 'children':[]}

# value8 ={'value':8, 'children':[]}

# right ={'value':7, 'children':[value8]}

# t = {"value":3, 'children':[left, center, right]}

# print(len(t))

# def print_tree(t):

#     if len(t['children'])==0:
#         print(t['value'])
#     else:
#         print(t['value'])
#         for child in t['children']:
#             print_tree(child)

# print_tree(t)

class Tree(object):

    def __init__(self, key) -> None:
        
        self.right = None
        self.right2 = None

        self.left = None
        self.left2 = None

        self.val = key

root = Tree('0')

root.left = Tree('1')
root.right = Tree('2')
root.right2 = Tree('3')
root.left2 = Tree('4')

print(root.left.val)
print(root.right.val)
print(root.left2.val)
print(root.right2.val)
