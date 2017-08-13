class Solution(object):
	i_max=0
	
	@classmethod
	def jump(self,index,s,ans):
		if s[index]+index<len(ans):
			for i in range(ans.index(0),s[index]+index):
				ans[i]=s[i]+i
		else:
			Solution.i_max=len(ans)
		if max(ans)>Solution.i_max:
			Solution.i_max=max(ans)
			if Solution.i_max<len(ans)-1:
				self.jump(Solution.i_max,s,ans)
			
	@classmethod
	def canJump(self, nums):
		Solution.i_max=0
		ans=[0]*len(nums)
		i=0
		if len(nums)==1:
			return True
		while nums[i]==1:
			i+=1
			if i==len(nums):
				return True
		self.jump(0,nums,ans)
		print Solution.i_max
		if Solution.i_max>=len(nums)-1:
			return True
		else:
			return False
		
			
aa=[2,3,1,1,4]	
bb=[3,2,1,0,4]	
dd=[1]
ee=[5,9,3,2,1,0,2,3,3,1,0,0]
cc=[8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]	
print Solution().canJump(dd)
		
