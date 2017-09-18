class Solution(object):
	def numDistinct(self, s, t):
		if len(s)<len(t):
			return 0
		ans=[]
		tmp=[]
		for j in range(len(s)):
			ans.append(0)
		for i in range(len(t)):
			tmp.append(list(ans))
		if s.find(t[0])==-1:
			return 0
		tmp[0][s.index(t[0])]=1
		for i in range(len(t)):
			for j in range(s.index(t[0])+1,len(s)):
				if s[j]==t[i]:
					if i==0:
						tmp[i][j]=tmp[i][j-1]+1
					else:
						tmp[i][j]=tmp[i-1][j-1]+tmp[i][j-1]
				else:
					tmp[i][j]=tmp[i][j-1]
		return tmp[-1][-1]
s='b'	
t='b'

#~ s='rabbbit'
#~ t='rabbit'
print Solution().numDistinct(s,t)
			
