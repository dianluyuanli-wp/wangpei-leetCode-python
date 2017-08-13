class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	max_n=float('-inf')
	
	@classmethod
	def maxPathSum_my(self, root):
		if root is None: 
			return 0
		l_max=self.maxPathSum_my(root.left)
		r_max=self.maxPathSum_my(root.right)
		Solution.max_n=max(l_max+r_max+root.val,Solution.max_n)
		v_r=root.val+max(l_max,r_max)
		return v_r if v_r>0 else 0
		
	@classmethod
	def maxPathSum(self, root):
		Solution.max_n=float('-inf')
		a=self.maxPathSum_my(root)
		return Solution.max_n
		

		
p1=TreeNode(8)
p2=TreeNode(9)
p3=TreeNode(-6)
p4=TreeNode(5)
p5=TreeNode(9)
p6=TreeNode(8)
p7=TreeNode(13)
p8=TreeNode(4)
p9=TreeNode(1)

p1.left=p2
p1.right=p3
p3.left=p4
p3.right=p5

#~ p3.right=p5
#~ p6.left=p7
#~ p6.right=p8
#~ p8.rightn=p9

print Solution().maxPathSum(p1)
