class Solution(object):
	def climbStairs(self, n):
		sum_n=1
		sum_p=0
		for i in range(n):
			tmp=sum_n
			sum_n=sum_p+sum_n
			sum_p=tmp
		return sum_n
		
print Solution().climbStairs(9)
