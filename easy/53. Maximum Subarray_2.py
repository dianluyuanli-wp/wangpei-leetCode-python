class Solution(object):
	def maxSubArray(self, nums):
		sum_n=nums[0]
		max_n=nums[0]
		for i in range(1,len(nums)):
			sum_n=max(nums[i],sum_n+nums[i])
			if sum_n>max_n:
				max_n=sum_n
		return max_n
		
a=[1]
print Solution().maxSubArray(a)
				
