class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		
		if head is None:
			return None
		if head.next is None:
			return head
			
		p=head
		q=head.next
		ans=head.next
		
		p.next=q.next
		q.next=p
		if p.next is None:
			return ans
		w=p
		if w.next.next is None:
			return ans
		p=w.next
		q=p.next
		
		while q.next is not None:
			p.next=q.next
			q.next=p
			w.next=q
			w=p
			p=p.next
			if p.next is None:
				return ans
			q=p.next
		if q.next is None:
			p.next=q.next
			q.next=p
			w.next=q
		return ans
		
l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)
l6=ListNode(6)
l7=ListNode(7)
l8=ListNode(8)

l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=l6
l6.next=l7
#~ l7.next=l8

ans=Solution().swapPairs(l1)

while ans is not None:
	print ans.val
	ans=ans.next

		

			
