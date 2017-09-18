class Solution(object):
	def isInterleave(self, s1, s2, s3):
		if len(s1)+len(s2)!=len(s3):
			return False
		if s1=='' or s2=='':
			if s1+s2==s3:
				return True
			else:
				return False
		stack=[]
		stack.append(s3.find(s1[0]))
		index=0
		hook=[]
		hook.append(stack[-1])
		while len(stack)!=0:
			while len(stack)!=len(s1):
				if len(hook)==len(stack):
					index=s3.find(s1[len(stack)],hook[len(stack)-1]+1)
				else:
					index=s3.find(s1[len(stack)],hook[len(stack)]+1)
				if index!=-1:
					stack.append(index)
					if len(hook)<len(stack):
						hook.append(stack[-1])
					else:
						hook[len(stack)-1]=index
						while len(hook)>len(stack):
							hook.pop()
				else:
					break
			if len(stack)==len(s1):
				left=list(s3)
				for i in stack:
					left[i]=''
				a=''.join(left)
				if a==s2:
					return True
			stack.pop()
			if len(stack)==0 and s3.find(s1[0],hook[0]+1)!=-1:
				stack.append(s3.find(s1[0],hook[0]+1))
				hook=[]
				hook.append(stack[-1])
		return False

					
		
