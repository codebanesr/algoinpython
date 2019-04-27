# check if the trees are identical or not

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None



def identicalTrees(root1, root2):
	if root1==None and root2==None:
		return True

	q1=[]
	q2=[]

	while True:
		q1.append(root1)
		q2.append(root2)

		while len(q1)>0 and len(q2)>0:
			node1 = q1[0]
			q1.pop(0)

			node2 = q2[0]
			q2.pop(0)

			if node1.data!=node2.data:
				return False
			
			if node1.left is not None:
				q1.append(node1.left)

			if node1.right is not None:
				q1.append(node1.right)

			if node2.left is not None:
				q2.append(node2.left)

			if node2.right is not None:
				q2.append(node2.right)
		
		if len(q1)==0 and len(q2)==0:
			return True
		else:
			return False


if __name__ == '__main__': 
    root1 = Node(1)  
    root1.left = Node(2)  
    root1.right = Node(3)  
    root1.left.left = Node(4)  
    root1.left.right = Node(5)  
  
    root2 = Node(1)  
    root2.left = Node(2)  
    root2.right = Node(3)  
    root2.left.left = Node(4)  
    root2.left.right = Node(5)  
  
    if identicalTrees(root1, root2): 
        print("Yes") 
    else: 
        print("No") 


			
