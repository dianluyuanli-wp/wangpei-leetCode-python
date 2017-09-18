class Solution(object):
	def rec_jie(self,n):
		if n is 0:
			return 1
		return n*self.rec_jie(n-1)
		
	def climbStairs(self, n):
		num=0
		for i in range(n//2+1):
			num+=self.rec_jie(i+n-2*i)/self.rec_jie(i)/self.rec_jie(n-2*i)
		return num
		
print Solution().climbStairs(7)
