class Solution(object):
	def jiemul(self,x):
		if x==0:
			return 1
		return x*self.jiemul(x-1)
	def uniquePaths(self, m, n):
		return self.jiemul(m+n-2)/self.jiemul(n-1)/self.jiemul(m-1)
		
print  Solution().uniquePaths(22,33)
