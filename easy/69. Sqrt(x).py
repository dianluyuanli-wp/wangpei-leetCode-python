class Solution(object):
	def mySqrt(self, x):
		ans=x
		ans_2=0
		if x==0:
			return 0
		while abs(ans-ans_2)>1e-3:
			ans_2=ans
			ans=ans/2.0+x/2.0/ans
		return round(ans)
		
print Solution().mySqrt(0)
