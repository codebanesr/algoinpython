class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left), height(root.right))


def spiralOrderTraversal(root):
    if root is None:
        return
    h = height(root)
    ltr = True
    for i in range(1, h+1):
        levelOrder(root, i, ltr)
        ltr = not ltr

def levelOrder(root, level, ltr):
    if level == 1:
        print(root.data, end=", ")
        return

    if ltr==True:
        levelOrder(root.left, level-1, ltr)
        levelOrder(root.right, level-1, ltr)
    else:
        levelOrder(root.right, level-1, ltr)
        levelOrder(root.left, level-1, ltr)



root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(61)
root.left.right = Node(62)

root.right.left = Node(91)
root.right.right = Node(92)

spiralOrderTraversal(root)
