class Solution(object):
	def add_one(self,i,list_n):
		if list_n[i]+1==10:
			list_n[i]=0
			if i==-len(list_n):
				list_n.insert(0,1)
			else:
				self.add_one(i-1,list_n)
		else:
			list_n[i]+=1
		return list_n
		
	def plusOne(self, digits):
		return self.add_one(-1,digits)
		
		
aa=[9,9,9,9]
print Solution().plusOne(aa)
