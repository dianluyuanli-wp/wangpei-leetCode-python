class Solution(object):
	def maxSubArray(self, nums):
		if len(nums) ==1:
			return nums[0]
		sum_n=0
		ans=[]
		flag=0
		while 0 in nums:
			flag=1
			nums.remove(0)
			
		for i in range(len(nums)-1):
			if (nums[i]>0) != (nums[i+1]>0):
				sum_n+=nums[i]
				ans.append(sum_n)
				sum_n=0
			else:
				sum_n+=nums[i]
		sum_n+=nums[-1]
		ans.append(sum_n)
		#print ans
		
		if len(ans)==1 and nums[0]<0:
			if flag==1:
				return 0
			return max(nums)
		if len(ans)==1 and nums[0]>0:
			return ans[0]
		max_n=ans[0] if ans[0]>ans[1] else ans[1]
		sum_n=max_n
		flag=1
		if ans[0]<0:
			flag=2
		for i in range(flag,len(ans)):
			if ans[i]+sum_n>0:
				sum_n+=ans[i]
				if sum_n>max_n:
					max_n=sum_n
			else:
				sum_n=0
		print 'flag'+str(flag)
		if max_n<0 and flag==1:
			max_n=0
		return max_n
		
aa=[-1,0]
print Solution().maxSubArray(aa)
				
				
			
				
		
