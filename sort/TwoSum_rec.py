class Solution(object):

	def qsort_rec(self,lst,l,r):
		if l>=r:
			return
		i=l
		j=r
		pivot=lst[i]
		while i<j:
			while i<j and lst[j]>=pivot:
				j-=1
			if i<j:
				lst[i]=lst[j]				
				i+=1						
			while i<j and lst[i]<=pivot:
				i+=1
			if i<j:
				lst[j]=lst[i]
				j-=1
		lst[i]=pivot
		self.qsort_rec(lst,l,i-1)		
		self.qsort_rec(lst,i+1,r)	
		
	def twoSum(self, nums, target):
		nums_s=list(nums)
		self.qsort_rec(nums_s,0,len(nums)-1)
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
						if nums[m]==nums_s[j]:
							break
					return [n,m]
				j+=1
						
nums = [3,2,4]
			
print(Solution().twoSum(nums,6))
        
