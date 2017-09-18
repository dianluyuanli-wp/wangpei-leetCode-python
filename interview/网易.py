a='aaabbaaac'
stack=[]
s_len=1
ans=[]
while True:
	try:
		a=raw_input()
		if not a:
			break 
		s_len=1
		ans=[]
		stack=[]
		for i in range(len(a)):
			if i !=len(a)-1:
				if a[i]==a[i+1]:
					s_len+=1
				else:
					ans.append(s_len)
					s_len=1
			else:
				if a[i]==a[i-1]:
					ans.append(s_len)
				else:
					ans.append(1)
		#print ans
		bb=round(1.0*sum(ans)/(len(ans))*1.0,2)
		print ('%.2f'% bb)
	except:
		break
