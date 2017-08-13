class Solution(object):
	def isPalindrome(self, x):
		test=str(x)
		print(test)
		
		test_rev=test[::-1]
		return True if test==test_rev else False

aa=-2147483648
print(Solution().isPalindrome(aa))
