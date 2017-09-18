point=[]
sort_point=point.sort()

sort_ans=[]
for x in point:
	sort_ans.append(x.value)
	
point_cc=list(sort_ans)
point_cc.sort()

ans=[]
for x in point_cc:
	ans.append(sort_ans.index(x))

for x in ans:
	if ok_num<n:
		ok_num+=point[x].num
		if ok_num>=n:
			return point[x].value

	
