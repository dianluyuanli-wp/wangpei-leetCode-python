COUNT=0
ans=[]
def perm(n,begin,end):
	global COUNT
	tmp=''
	if begin>=end:
		for i in range(len(n)):
			tmp+=n[i]
		ans.append(tmp)
		COUNT +=1
	else:
		i=begin
		for num in range(begin,end):
			n[num],n[i]=n[i],n[num]
			perm(n,begin+1,end)
			n[num],n[i]=n[i],n[num]
 
n=['1','2', '4','4']
b=4

reduce(lambda x, y:[z0 + z1 for z0 in x for z1 in y], [n] * (b - 1), n)
#perm(n,0,len(n))
#vv=list(set(ans))
print COUNT
#print(vv)

