class Solution(object):
	stack=[]
	ans=[]
	
	def rec(self,l,last,lis):
		start=self.stack.index([l,l+1])
		end=self.stack.index([l+1,l+2])
		for i in self.stack[start:end]:
			add_l=list(last)
			add_l.append(lis[i[0]:i[1]])
			if i[1]==len(lis):
				self.ans.append(add_l)
			elif self.stack.index([i[1],i[1]+1])==len(self.stack)-1:
				add_l.append(lis[-1])
				self.ans.append(add_l)
			else:
				self.rec(i[1],add_l,lis)
			
	def ispa(self,left,right,s):
		while s[left]==s[right] :
			if s[left:right+1] not in self.stack:
				self.stack.append([left,right+1])
			left-=1
			right+=1
			if left<0 or right>len(s)-1:
				break
	
	def partition(self, s):
		self.stack=[]
		self.ans=[]
		if len(s)==1:
			a=[]
			a.append(s)
			self.ans.append(a)
			return self.ans
		for i in range(len(s)):
			self.ispa(i,i,s)
			if i!=len(s)-1:
				self.ispa(i,i+1,s)
		self.stack.sort()
		self.rec(0,[],s)
		return self.ans
	
aa="cbbc"
print Solution().partition(aa)
