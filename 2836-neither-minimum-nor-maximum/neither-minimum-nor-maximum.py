class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_ele = max(nums)
        min_ele = min(nums)
        for ch in nums:
            if ch != max_ele and ch != min_ele:
                return ch
        return -1

        