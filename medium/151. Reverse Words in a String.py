class Solution(object):
	def reverseWords(self, s):
		aa=s.split()
		aa.reverse()
		ans=""
		for ii in aa:
			ans+=ii+' '
		return ans[0:-1]

aa="the sky is blue"
print Solution().reverseWords(aa)
