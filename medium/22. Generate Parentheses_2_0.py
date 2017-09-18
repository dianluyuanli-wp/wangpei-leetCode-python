class Solution(object):
	ans=[]
	@classmethod
	def kuohao(self,my,p,n):
		if n>p:
			my_tt=my
			if p>=1:
				my+='('
				self.kuohao(my,p-1,n)
			if n>=1:
				my_tt+=')'
				self.kuohao(my_tt,p,n-1)
		elif n==p and n!=0:
			my+='('
			self.kuohao(my,p-1,n)
		if n==0 and p==0:
			#print my
			Solution.ans.append(my)
			
	@classmethod	
	def generateParenthesis(self, n):
		Solution.ans=[]
		self.kuohao('',n,n)
		return Solution.ans
		
print Solution().generateParenthesis(7)
