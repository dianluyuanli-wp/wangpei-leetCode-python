class Solution(object):
	def isValid(self, s):
		stack=[]
		for i in range(len(s)):
			if s[i] in '({[':
				stack.append(s[i])
			elif stack:
				if '({['.find(stack[-1])==')}]'.find(s[i]):
					stack.pop()
				else:
					return False
			else:
				return False
		if stack:
			return False
		return True
		
print Solution().isValid('()(')
				
				
			
