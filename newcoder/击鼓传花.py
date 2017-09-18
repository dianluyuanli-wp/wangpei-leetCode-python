a=30
ci=30
tt=[]
num=[]
for i in range(a):
	tt.append(0)
for i in range(ci+1):
	num.append(list(tt))
	
print len(num)
print len(num[0])


num[0][0]=1
for i in range(1,ci+1):
	for j in range(a):
		if j==0:
			num[i][j]=num[i-1][j+1]+num[i-1][a-1]
		elif j==a-1:
			num[i][j]=num[i-1][0]+num[i-1][j-1]
		else:
			num[i][j]=num[i-1][j+1]+num[i-1][j-1]
#print num
print num[-1][0]
