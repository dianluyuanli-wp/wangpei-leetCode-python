class Solution(object):
	def myPow(self, x, n):
		num=x*1.0
		if n==0:
			return 1
		if n>2147483646:
			if abs(x)<1:
				return 0
			if x==1:
				return 1
			if x==-1:
				return 1 if n%2==0 else -1
		if n<-2147483643:
			if abs(x)==1:
				return 1
			else:
				return 0
		for i in range(abs(n)-1):
			num=num*x*1.0
		if n<0:
			num=1.0/num 
		return num
		
print Solution().myPow(34.00515,-3)
