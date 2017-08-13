class Solution(object):
	def searchInsert(self, nums, target):
		if target in nums:
			return nums.index(target)
		if target>nums[-1]:
			return len(nums)
		if target<nums[0]:
			return 0
		min_l=0
		max_l=len(nums)-1
		while max_l-min_l!=1:
			mid=min_l+(max_l-min_l)//2
			if target>nums[mid]:
				min_l=mid
			else:
				max_l=mid
		return max_l
