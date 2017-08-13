class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def com_bv(self,node):
		#print node.val
		if node.left is None and node.right is None:
			node.bv=0
		elif node.left is None and node.right is not None:
			node.bv=self.com_bv(node.right)+1
		elif node.left is not None and node.right is None:
			node.bv=self.com_bv(node.left)+1
		else:
			left_n=self.com_bv(node.left)
			right_n=self.com_bv(node.right)
			node.bv=left_n+1 if left_n>right_n else right_n+1
		return node.bv
		
	def isBalanced(self, root):
		if not root:
			return True
		a=self.com_bv(root)
		stack=[]
		r_node=root
		while r_node is not None or stack:
			#print str(r_node.val)+' '+str(r_node.bv)
			if r_node.left is not None and r_node.right is not None:
				if abs(r_node.left.bv-r_node.right.bv)>1:
					return False
			if r_node.left is None and r_node.right is not None:
				if abs(0-r_node.right.bv-1)>1:
					return False
			if r_node.left is not None and r_node.right is None:
				if abs(1+r_node.left.bv)>1:
					return False
			if r_node.right is not None:
				stack.append(r_node.right)
			r_node=r_node.left
			if r_node is None and stack:
				r_node=stack.pop()
		return True
		
p1=TreeNode(1)
p2=TreeNode(2)
p3=TreeNode(3)
p4=TreeNode(4)
p5=TreeNode(5)
p6=TreeNode(6)
p7=TreeNode(7)
p8=TreeNode(8)
p9=TreeNode(9)

p1.right=p2
p2.right=p3
#~ p5.left=p2
#~ p5.right=p7
#~ p2.left=p1
#~ p2.right=p4
#~ p4.left=p3
#~ p7.left=p6
#~ p7.right=p9
#~ p9.left=p8

print Solution().isBalanced(p1)
