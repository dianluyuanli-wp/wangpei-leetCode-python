class Solution(object):
	def evalRPN(self, tokens):
		tokens.reverse()
		a=tokens
		stack=[]
		for x in a:
			stack.append(x)
		com=[]
		#print stack
		operate=['+','-','*','/']
		while stack :
			op=stack.pop()
			if op not in operate:
				#print op
				com.append(int(op))
			else:
				op_a=com.pop()
				op_b=com.pop()
				if op=='+':
					ans=op_a+op_b
				if op=='-':
					ans=op_b-op_a
				if op=='*':
					ans=op_a*op_b
				if op=='/':
					ans=op_b//op_a
					if ans<0 and op_b%op_a!=0:
						ans+=1
				#print ans
				com.append(ans)
		return com.pop()

aa=["4","-2","/","2","-3","-","-"]
print Solution().evalRPN(aa)
