# -*- coding:utf-8 -*-
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		
class Solution:
	def modi(self,tin_node,tin_list,pre):
		if len(tin_node)==1:
			return tin_node[0]
			
		for i in range(len(pre)):
			if pre[i] in tin_list:
				index=tin_list.index(pre[i])
				if len(tin_node[:index])>0:
					tin_node[index].left=self.modi(tin_node[:index],tin_list[:index],pre)
				if len(tin_node[index+1:])>0:
					tin_node[index].right=self.modi(tin_node[index+1:],tin_list[index+1:],pre)
				return tin_node[index]
					
	def reConstructBinaryTree(self, pre, tin):
		tin_node=[]
		for i in tin:
			tr_node=TreeNode(i)
			tin_node.append(tr_node)
		r_in=tin.index(pre[0])
		if len(tin_node[:r_in])>0:
			tin_node[r_in].left=self.modi(tin_node[:r_in],tin[:r_in],pre)
		if len(tin_node[r_in:])>0:
			tin_node[r_in].right=self.modi(tin_node[r_in+1:],tin[r_in+1:],pre)
		return tin_node[r_in]
				
pre=[1,2,4,7,3,5,6,8]
tin=[4,7,2,1,5,3,8,6]
aa=Solution().reConstructBinaryTree(pre,tin)
print(aa.left.left.right.val)
