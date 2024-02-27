class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        max_ele = max(nums)
        for i in range(n):
            if nums[i] == max_ele:
                return i

        