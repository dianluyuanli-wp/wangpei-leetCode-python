class Solution(object):
	def merge(self,lfrom,lto,low,mid,high):					
		i,j,k=low,mid,low							
		while i<mid and j<high:						
			if lfrom[i]<=lfrom[j]:
				lto[k]=lfrom[i]
				i+=1
			else:
				lto[k]=lfrom[j]					
				j+=1							
			k+=1
		while i < mid:
			lto[k]=lfrom[i]
			i+=1
			k+=1
		while j<high:
			lto[k]=lfrom[j]
			j+=1
			k+=1

	def merge_pass(self,lfrom,lto,llen,slen):				
		i=0											
		while i+2*slen<llen:							
			self.merge(lfrom,lto,i,i+slen,i+2*slen)
			i+=2*slen
		if i+slen<llen:								
			self.merge(lfrom,lto,i,i+slen,llen)
		else:
			for j in range(i,llen):							
				lto[j]=lfrom[j]

	def merge_sort(self,lst):
		slen,llen=1,len(lst)
		templst=[None]*llen
		while slen<llen:								
			self.merge_pass(lst,templst,llen,slen)	
			slen*=2
			self.merge_pass(templst,lst,llen,slen)
			slen*=2
			
	def twoSum(self, nums, target):
		nums_s=list(nums)
		self.merge_sort(nums_s)
		for i in range(len(nums_s)):
			j=i+1
			if nums_s[i]+nums_s[-1]<target:
				continue
			while j<len(nums_s):
				if nums_s[i]+nums_s[j]==target:
					for n in range(len(nums)):
						if nums[n]==nums_s[i]:
							break
					for m in range(len(nums)):
						if nums[m]==nums_s[j] and m is not n:
							break
					return [n,m]
				j+=1
						
nums = [3,3]
			
print(Solution().twoSum(nums,6))
        
