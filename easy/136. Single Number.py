class Solution(object):
	def singleNumber(self, nums):
		aa=nums[0]
		for i in range(0,len(nums)-1):
			#print nums[i]
			aa=aa^nums[i+1]
		return aa
		#~ my_c=sorted(nums)
		#~ print my_c
		#~ if len(my_c) is 1:
			#~ return my_c[0]
		#~ for i in range(0,len(nums)-1,2):
			#~ if my_c[i] != my_c[i+1]:
				#~ return my_c[i]
		#~ return my_c[-1]
	
aa=[17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]	
bb=[1]	
print Solution().singleNumber(aa)
			
