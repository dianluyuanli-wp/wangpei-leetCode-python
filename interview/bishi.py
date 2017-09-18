d=['i','like','ali','liba','baba','alibaba']
s=''

l_s=[]
test=[]
for i in d:
	if len(i) not in l_s:
		l_s.append(len(i))
		test.append([i])
	else:
		for j in test:
			if len(j[0])==len(i):
				j.append(i)

l_s_c=list(l_s)
l_s_c.sort()
ans=[]
for i in l_s_c:
	ans.append(l_s.index(i))

print ans
print  l_s		
print test

#~ for i in range(len(

