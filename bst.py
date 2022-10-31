

class Tree:

    def __init__(self, key) -> None:
        
        self.val = key
        self.left = None
        self.right = None


def insert(root, key):

    if root is None:
        return Tree(key)
    
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    
    return root

def preorder(root):
    
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root):
    
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def search(root, key):

    if root is None or root.val==key:
        return root

    if root.val < key:
        return search(root.right, key)
    
    return search(root.left, key)

root = Tree(50)

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# inorder(root)
# preorder(root)
# postorder(root)

print(search(root, 81) is not None)