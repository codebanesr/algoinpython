# check if the trees are identical or not

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def identicalTrees(root1, root2):
	if root1 is None and root2 is None:
		return True
	if root1.data == root2.data and root1.data == root2.data:
		return identicalTrees(root1.left, root2.left) and identicalTrees(root1.right, root2.right)
	return False

# Driver program to test identicalTress function 
root1 = Node(1) 
root2 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
  
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5) 
  
if identicalTrees(root1, root2): 
    print( "Both trees are identical")
else: 
    print ("Trees are not identical")
