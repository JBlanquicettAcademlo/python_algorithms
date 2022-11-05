class Node:

    def __init__(self, key):
        
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node[{self.key}]'


def insert(node, key):

    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    else:
        node.right = insert(node.right, key)

    return node


def search(node, key):

    if node is None:
        return node

    if key == node.key:
        return node

    if key > node.key:
        return search(node.right, key)

    if key < node.key:
        return search(node.left, key)

def min_value_node(node):
    current = node
    while current.left is not None:
        current=current.left
    return current

def max_value_node(node):
    current = node
    while current.right is not None:
        current=current.right
    return current

def delete_node(root, key):

    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key

        root.right = delete_node(root.right, temp.key)

    return root


root = None
root = insert(root, 12)
root = insert(root, 23)
root = insert(root, 9)
root = insert(root, 10)

# print(min_value_node(root))
# print(max_value_node(root))

ok=search(root, 9)
print(ok)
root=delete_node(root, 9)
ok=search(root, 9)
print(ok)

ok=search(root, 10)
print(ok)
ok=search(root, 23)
print(ok)
ok=search(root, 12)
print(ok)
