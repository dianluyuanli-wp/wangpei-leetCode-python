class Solution(object):
	def isPalindrome(self, s):
		aa=filter(str.isalnum,s)
		cc=aa.lower()
		bb=cc[::-1]
		if bb == cc:
			return True
		else:
			return False

aa=" "	
print(Solution().isPalindrome(aa))
