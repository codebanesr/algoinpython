class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None



# this works using level order traversal
def height(root):
	if root is None:
		return 0
	q = []
	height = 0
	q.append(root)
	while True:
		# node count
		nc=len(q)
		if nc == 0:
			return height
		height=height+1
		while nc>0:
			node = q[0]
			q.pop(0)
			if node.left is not None:
				q.append(node.left)
			if node.right is not None:
				q.append(node.right)
			nc=nc-1


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print ("Height of tree is", height(root)) 

