class Solution(object):
	def spiralOrder(self, matrix):
		if not matrix:
			return []
		m=len(matrix)
		n=len(matrix[0])
		m_1,n_1,m_2,n_2=m,n,0,0
		ans=[]
		status=1
		i,j=0,0
		for x in range(m*n):
			if status==1:
				if j<n_1:
					ans.append(matrix[i][j])
					j+=1
				else:
					j-=1
					m_1-=1
					i+=1
					ans.append(matrix[i][j])
					status=2
					m_2+=1
			elif status==2:
				if i<m_1:
					i+=1
					ans.append(matrix[i][j])
				else:
					n_1-=1
					j-=1
					ans.append(matrix[i][j])
					status=3
			elif status==3:
				if j>n_2:
					j-=1
					ans.append(matrix[i][j])
				else:
					i-=1
					ans.append(matrix[i][j])
					status=4
			elif status==4:
				if i>m_2:
					i-=1
					ans.append(matrix[i][j])
				else:
					j+=1
					ans.append(matrix[i][j])
					j+=1
					status=1
					n_2+=1
		return ans
					
aa=[
 [ 1, 2, 3 , 4],
 [ 5, 6 ,7 , 8],
 [ 9,10,11,12 ],
 [13,14, 15,16]
]
bb=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
cc=[[1,2],
[3,4]]
print Solution().spiralOrder(aa)
					
