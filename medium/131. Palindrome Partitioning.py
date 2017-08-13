class Solution(object):
	stack=[]
	
	@classmethod
	def ispa(self,l,r,s):
		while s[l]==s[r] :
			if s[l:r+1] not in Solution.stack:
				Solution.stack.append(s[l:r+1])
			l-=1
			r+=1
			if l<0 or r>len(s)-1:
				break
	@classmethod
	def partition(self, s):
		for i in range(len(s)-1):
			self.ispa(i,i,s)
			self.ispa(i,i+1,s)
		if s[-1] not in Solution.stack:
			Solution.stack.append(s[-1])
		return Solution.stack
	
aa='aab'
print Solution().partition(aa)
