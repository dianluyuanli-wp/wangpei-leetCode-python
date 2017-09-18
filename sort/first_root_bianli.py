class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
def first_root(node):
	stack=[]
	while node is not None or stack:	
		if node is not None:
			stack.append(node.right)
			print node.val
			node=node.left
			continue
		elif stack:
			node=stack.pop()
			
p1=TreeNode(1)
p2=TreeNode(2)
p3=TreeNode(3)
p4=TreeNode(4)
p5=TreeNode(5)
p6=TreeNode(6)
p7=TreeNode(7)
p8=TreeNode(8)
p9=TreeNode(9)

p5.left=p2
p5.right=p7
p2.left=p1
p2.right=p4
p4.left=p3
p7.left=p6
p7.right=p9
p9.left=p8

first_root(p5)

