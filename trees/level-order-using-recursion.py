class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left), height(root.right))


def levelUsingRecursion(root):
    if root is None:
        return
    h = height(root)
    for i in range(1, h+1):
        levelOrder(root, i)

def levelOrder(root, level):
    if level == 1:
        print(root.data, end=", ")
    else:
        levelOrder(root.left, level-1)
        levelOrder(root.right, level-1)



root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(61)
root.left.right = Node(62)

root.right.left = Node(91)
root.right.right = Node(92)

levelUsingRecursion(root)
