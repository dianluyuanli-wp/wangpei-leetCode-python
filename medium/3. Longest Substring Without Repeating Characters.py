class Solution(object):
	def lengthOfLongestSubstring(self, s):
		stack=[]
		max_length=0
		for char in s:
			if char in stack:
				if len(stack)>max_length:
					max_length=len(stack)
				del stack[0:stack.index(char)+1]
				stack.append(char)
			else:
				stack.append(char)
		if len(stack)>max_length:
			max_length=len(stack)
		if len(s) is 1:
			max_length=1
		return max_length
		
aa='dvdf'		
print(Solution().lengthOfLongestSubstring(aa))
			

