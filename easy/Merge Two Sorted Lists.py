class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

a1=ListNode(2)
#~ a2=ListNode(3)
#~ a3=ListNode(5)
#~ a1.next,a2.next=a2,a3

b1=ListNode(1)
#~ b2=ListNode(4)
#~ b1.next=b2
#~ b3=ListNode(6)
#~ b1.next,b2.next=b2,b3

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if l1 is not None and l2 is not None:
			if l1.val>l2.val:
				l_1=l2
				l_2=l1
			else:
				l_1=l1
				l_2=l2
		else:
			l_1=l1
			l_2=l2
		while l_2 is not None:
			p=l_1
			flag=0
			q=l_1
			
			while p is not None and p.val<=l_2.val:
				q=p
				p=p.next
				flag=1
			if q is None:
				l_1=l_2
			else:
				q.next=l_2
			q=l_2
			if l_2 is not None:
				l_2=l_2.next
			q.next=p
		return l_1


cc=Solution().mergeTwoLists(a1,b1)
lst=[]
while cc.next is not None:
	lst.append(cc.val)
	cc=cc.next 
lst.append(cc.val)
print(lst)
