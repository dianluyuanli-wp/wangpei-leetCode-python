# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

a1=ListNode(2)
a2=ListNode(4)
a3=ListNode(3)
a1.next,a2.next=a2,a3

b1=ListNode(5)
b2=ListNode(6)
b3=ListNode(4)
b1.next,b2.next=b2,b3


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		a,b,c=[],[],[]
		carry=0
		a_flag=l1
		b_flag=l2
		
		while a_flag.next is not None:
			a.append(a_flag.val)
			a_flag=a_flag.next 
		a.append(a_flag.val)
		a.reverse()
		while b_flag.next is not None:
			b.append(b_flag.val)
			b_flag=b_flag.next 
		b.append(b_flag.val)
		b.reverse()
		
		num=len(a) if len(a)>=len(b) else len(b)
		if num>=len(b):
			while len(b)<len(a):
				b.insert(0,0)
		if num>=len(a):
			while len(a)<len(b):
				a.insert(0,0)

		for i in range(num):
			sum_n=a.pop()+b.pop()+carry
			carry=0
			if (sum_n)<10:
				c.append(sum_n)
				carry=0
			else:
				c.append(int((str(sum_n))[1]))
				carry=1
		if carry==1:
			c.append(1)
		#c.reverse()
		ans=[]
		for i in range(len(c)):
			node=ListNode(c[i])
			ans.append(node)
		for i in range(len(c)-1):
			ans[i].next=ans[i+1]
		return ans[0]

cc=Solution().addTwoNumbers(a1,b1)
lst=[]
while cc.next is not None:
	lst.append(cc.val)
	cc=cc.next 
lst.append(cc.val)
print(lst)
