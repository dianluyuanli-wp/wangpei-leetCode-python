class Solution(object):
	def pre(self,nums):
		max_p,min_p,p=float('-inf'),float('inf'),1
		for i in nums:
			p*=i
			if p>max_p:
				max_p=p
			if p<min_p:
				min_p=p
		if max_p<=0:
			max_p=1
		if min_p>=0:
			min_p=1
		return [max_p,min_p]
		
	def suf(self,nums):
		max_p,min_p,p=float('-inf'),float('inf'),1
		for i in range(-1,-len(nums)-1,-1):
			p*=nums[i]
			if p>max_p:
				max_p=p
			if p<min_p:
				min_p=p
		if max_p<=0:
			max_p=1
		if min_p>=0:
			min_p=1
		return [max_p,min_p]	
		
	def max_p(self,nums):
		if len(nums)==2:
			return max(nums[0],nums[1],nums[0]*nums[1])
		if len(nums)==1:
			return nums[0]
		mid=len(nums)//2
		suf_p=self.suf(nums[0:mid])
		pre_p=self.pre(nums[mid+1:len(nums)])
		if nums[mid]>0 :
			p1=(suf_p[0])*nums[mid]*(pre_p[0])
			p2=(suf_p[1])*nums[mid]*(pre_p[1])
			mid_p=max(p1,p2,nums[mid])
		if nums[mid]<=0:
			p1=(suf_p[0])*nums[mid]*(pre_p[1])
			p2=(suf_p[1])*nums[mid]*(pre_p[0])
			mid_p=max(p1,p2)
		l_nm=self.max_p(nums[0:mid])
		r_nm=self.max_p(nums[mid+1:len(nums)])
		return max(mid_p,l_nm,r_nm)
	def maxProduct(self, nums):
		return self.max_p(nums)
		
aa=[1,0,-1,2,3,-5,-2]
print Solution().maxProduct(aa)
