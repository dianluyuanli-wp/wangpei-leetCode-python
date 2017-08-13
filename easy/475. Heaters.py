class Solution(object):
	def findRadius(self, houses, heaters):
		houses.sort()
		heaters.sort()
		length=0
		for hou_i in houses:
			if hou_i>heaters[-1] or hou_i<heaters[0]:
				l_a=abs(hou_i-heaters[-1])
				l_b=abs(hou_i-heaters[0])
				length_t=l_a if l_a<l_b else l_b
				if length_t>length:
					length=length_t
				continue
			h_h=len(heaters)-1
			h_l=0
			if len(heaters) is 1:
				continue
			while h_h-h_l is not 1:
				heat_m=h_l+(h_h-h_l)//2
				if houses[i]>=heaters[heat_m]:
					h_l=heat_m
				else:
					h_h=heat_m
			while hou_i>heaters[h_l]+length and hou_i<heaters[h_h]-length:
				l_a=hou_i-heaters[h_l]
				l_b=heaters[h_h]-hou_i
				length_t=l_a if l_a<l_b else l_b
				if length_t>length:
					length=length_t
		return length
h=[1,2,3,4]
heat=[1,4]
print(Solution().findRadius(h,heat))
