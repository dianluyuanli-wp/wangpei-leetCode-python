s=''
a=0
for i in range(len(s)):
	if s[i]=='A':
		a+=1
	if s[i]=='L':
		if i!=0:
			l+=1
