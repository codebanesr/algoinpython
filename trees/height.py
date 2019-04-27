class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None



def height(root):
	if root is None:
		return 0
	return 1+( max(height(root.left), height(root.right)) )


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.right.right = Node(5)

print(height(root))
