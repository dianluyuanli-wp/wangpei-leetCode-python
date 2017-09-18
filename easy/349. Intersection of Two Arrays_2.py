class Solution(object):
    def intersection(self, nums1, nums2):
        ans=list(set(nums1)&set(nums2))
        return ans
