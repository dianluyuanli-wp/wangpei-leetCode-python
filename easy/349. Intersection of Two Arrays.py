class Solution(object):
    def intersection(self, nums1, nums2):
        nums1,nums2=set(nums1),set(nums2)
        ans=[]
        if len(nums1)<len(nums2):
            nums1,nums2=nums2,nums1
        for i in nums1:
            if i in nums2 and i not in ans:
                ans.append(i)
        return ans
                
