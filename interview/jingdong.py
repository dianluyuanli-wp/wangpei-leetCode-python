def rec(str_s):
	if len(str_s)==2:
		return 1
	else:
		if str_s[1]==')':
			return rec(str_s[2:])
		else:
			index=0
			str_li=list(str_s)
			sum_ll=0
			for i in range(len(str_s)/2):
				str_li=list(str_s)
				index=str_li.index(')',index+1)
				str_li[0]=''
				str_li[index]=''
				tt=''.join(str_li)
				sum_ll+=rec(tt)
			return sum_ll
			
while True:		
	try:
		a=raw_input()
		if not a:
			break
		stack=[]
		ans=[]
		sum_ll=1
		for i in range(len(a)):
			if a[i]=='(':
				stack.append(a[i])
			else:
				stack.pop()
			if len(stack)==0:
				ans.append(i)
		start=0
		for i in ans:
			sum_ll*=rec(a[start:i+1])
			start=i+1
		print sum_ll
	except:
		break
		
