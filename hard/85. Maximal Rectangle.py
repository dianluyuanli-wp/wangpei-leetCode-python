class Solution(object):
	def maximalRectangle(self, matrix):
		if not matrix:
			return 0
		for i in range(len(matrix)):
			matrix[i]=map(int,list(matrix[i]))
		hang_n=len(matrix)
		lie_n=len(matrix[0])
		ans=[]
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j]==0:
					ans.append(0)
					continue
				elif 0 not in matrix[i][j:]:
					lie=lie_n-j
				else:
					lie=matrix[i].index(0,j)-j
				for k in range(i,hang_n):
					if matrix[k][j]==0:
						area=(k-i)*lie
						ans.append(area)
						break
					elif 0 not in matrix[k][j:] and hang_n!=1 and k!=hang_n-1:
						continue
					elif hang_n!=1 and k!=hang_n-1 and matrix[k].index(0,j)-j<lie:
						ans.append(lie*(k-i))
						lie=matrix[k].index(0,j)-j
					if k==hang_n-1: 
						if 0 in matrix[k][j:] and matrix[k].index(0,j)-j<lie:
							ans.append(lie*(k-i))
							lie=matrix[k].index(0,j)-j
					if k==hang_n-1:
						area=(k-i+1)*lie
						ans.append(area)
		return max(ans)
		
#a=["10100","10111","11111","10010"]
#a=['1']
#a=["11","11"]
#a=["10100","10111","11111","10010"]
#a=["11111111","11111110","11111110","11111000","01111000"]
a=["101101","111111","011011","111010","011111","110111"]
print Solution().maximalRectangle(a)
					
