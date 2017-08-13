class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def hasPathSum(self, root, sum):
		stack=[]
		s_stack=[]
		ans=[]
		r_sum=0
		if root is None:
			return False
		while root is not None or stack:
			if root is not None:
				r_sum+=root.val
				if root.right is not None:
					stack.append(root.right)
					s_stack.append(r_sum)
				if root.right is None and root.left is None:
					ans.append(r_sum)
				root=root.left
				continue
			if stack:
				root=stack.pop()
				r_sum=s_stack.pop()
		ans.append(r_sum)
		if sum in ans:
			return True
		else:
			return False

p1=TreeNode(1)
p2=TreeNode(-2)
p3=TreeNode(3)
p4=TreeNode(4)
p5=TreeNode(5)
p6=TreeNode(6)
p7=TreeNode(7)
p8=TreeNode(8)
p9=TreeNode(9)

p1.left=p2
p1.right=p3
#~ p5.left=p2
#~ p5.right=p7
#~ p2.left=p1
#~ p2.right=p4
#~ p4.left=p3
#~ p7.left=p6
#~ p7.right=p9
#~ p9.left=p8			

print Solution().hasPathSum(p1,-1)
			
