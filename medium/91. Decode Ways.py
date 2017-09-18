class Solution(object):
	def rec_jie(self,n):
		if n is 0:
			return 1d
		return n*self.rec_jie(n-1)
		
	def climbStairs(self, n):
		num=0
		for i in range(n//2+1):
			num+=self.rec_jie(i+n-2*i)/self.rec_jie(i)/self.rec_jie(n-2*i)
		return num
		
	def numDecodings(self, s):
		if len(s)==0:
			return 0
		if s[0]=='0':
			return 0
		if s=='100':
			return 0
				
		kind=1
		index=0
		for i in range(len(s)):
			if int(s[i:i+2])>26 or int(s[i])==0:
				if int(s[i])==0 :
					if 0<int(s[i-1])<3:
						kind*=self.climbStairs(i-index)
					else:
						return 0
				else:
					kind*=self.climbStairs(i+1-index)
				index=i+1

			if i==len(s)-2:
				if s[i+1]=='0':
					#print 1000
					if 0<int(s[i])<3:
						kind*=self.climbStairs(i-index)
					else:
						return 0
				else:
					kind*=self.climbStairs(i+2-index)
				break
		return kind
		
a='130'
print Solution().numDecodings(a)
