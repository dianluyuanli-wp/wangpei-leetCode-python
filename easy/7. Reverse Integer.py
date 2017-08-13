class Solution(object):
	def reverse(self, x):
		str_n=str(x)
		ans=0
		if str_n[0] is '-':
			ans=0-int(str_n[1:][::-1])
		else:
			ans=int(str_n[::-1])
		if pow(2,31)>=ans>=(0-pow(2,31)):
			return ans
		else:
			return 0
			
aa=100
print Solution().reverse(aa)
