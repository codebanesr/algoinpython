class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def spiralOrderTraversal(root):
    ltr = [root]
    rtl = []

    while len(ltr)>0 or len(rtl)>0:
        while len(ltr) > 0:
            node = ltr.pop()
            print(node.data)
            if node.left:
                rtl.append(node.left)
            if node.right:
                rtl.append(node.right)
        while len(rtl)>0:
            node = rtl.pop()
            print(node.data)
            if node.right:
                ltr.append(node.right)
            if node.left:
                ltr.append(node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(61)
root.left.right = Node(62)

root.right.left = Node(91)
root.right.right = Node(92)

spiralOrderTraversal(root)
