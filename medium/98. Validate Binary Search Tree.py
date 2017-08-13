class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution(object):
	def middle_root(self,node):
		stack=[]
		flag=1
		num=[]
		#~ if node.left is None:
			#~ stack.append(node)
		while node is not None or stack:
			if node is not None and flag==1:
				if node.left is not None:
					stack.append(node)
					node=node.left
				else:
					num.append(node.val)
					node=node.right
				continue
			if node is not None and flag==0:
				num.append(node.val)
				node=node.right
				flag=1
			if node is None and stack:
				node=stack.pop()
				flag=0
		return num
		
	def isValidBST(self, root):
		num=self.middle_root(root)
		print num
		for i in range(len(num)-1):
			if num[i]>=num[i+1]:
				return False
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

p5.left=p2
p5.right=p7
p2.left=p1
p2.right=p4
p4.left=p3
p7.left=p6
p7.right=p9
p9.left=p8

#~ p1=TreeNode(1)
#~ p2=TreeNode(1)
#~ #p3=TreeNode(2)
#~ 
#~ p1.right=p2
#~ #p1.left=p3
print Solution().isValidBST(p5)
