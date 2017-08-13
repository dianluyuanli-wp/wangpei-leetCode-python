class Solution(object):			
	def minDepth(self, root):
		node=root
		stack=[]
		len_min=float('inf')
		if node is None:
			return 0
		node.length=1
		while node is not None or stack:	
			if node is not None:
				stack.append(node.right)
				if node.right is not None:
					node.right.length=node.length+1
				if node.left is not None:
					node.left.length=node.length+1
				if node.left is None and node.right is None:
					if node.length<len_min:
						len_min=node.length
				node=node.left
				continue
			elif stack:
				node=stack.pop()
		return len_min
