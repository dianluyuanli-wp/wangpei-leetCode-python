# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def my_rec(self,lst,start,end):
		length=end-start
		if length is 1:
			left_node=TreeNode(lst[start])
			r_node=TreeNode(lst[end])
			r_node.left=left_node
			return r_node
		elif length is 0:
			r_node=TreeNode(lst[end])
			return r_node
		else:
			root=TreeNode(lst[start+length//2])
			root.left=self.my_rec(lst,start,start+length//2-1)
			root.right=self.my_rec(lst,start+length//2+1,end)
			return root

	def sortedListToBST(self, head):
		link_l=[]
		while head is not None:
			link_l.append(head.val)
			head=head.next
		if len(link_l) is 0:
			return
		return self.my_rec(link_l,0,len(link_l)-1)

			

