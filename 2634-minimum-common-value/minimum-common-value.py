class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        li = []
        nums1 = set(nums1)
        for num in nums2:
            if num in nums1:
                li.append(num)
        if li:
            return min(li)
        return -1
        