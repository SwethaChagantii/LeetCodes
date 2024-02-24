class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        n = len(nums)
        nums = sorted(nums)
        if n % 2 == 0:
            median = (nums[(n-1)//2] + nums[((n-1)//2) + 1] ) / 2
        else:
            median = nums[(n-1)//2]
        return float(median)
        