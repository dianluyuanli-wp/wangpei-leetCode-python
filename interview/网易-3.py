a='(())(())()(((())))'
b=list(a)
ans=[]

def kuohao(string):
	stack=[]
	for i in range(len(string)):
		if string[i]=='(':
			stack.append(string[i])
		elif len(stack)!=0:
			stack.pop()
		else:
			return False
	if len(stack)==0:
		return True
	else:
		return False
		
for i in range(len(b)):
	c=list(b)
	char=c[i]
	del c[i]
	for j in range(len(b)):
		tmp=list(c)
		tmp.insert(j,char)
		tt=''.join(tmp)
		if tt==a:
			continue
		elif not kuohao(tt):
			continue
		elif tt not in ans:
			ans.append(tt)
			
print ans
		
