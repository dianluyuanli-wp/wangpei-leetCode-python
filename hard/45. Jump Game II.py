class Solution(object):
	def jump(self, nums):
		start,max_1,index,step=0,0,nums[0],0
		if len(nums)==1:
			return 0
		while index<len(nums)-1:
			for i in range(start,index+1):
				if max_1<i+nums[i]:
					max_1=i+nums[i]
			start=index+1
			index=max_1
			step+=1
		return step+1
		
aa=[5,9,3,2,1,0,2,3,3,1,0,0]
print Solution().jump(aa)
