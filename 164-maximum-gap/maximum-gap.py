class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_gap = 0
        num = sorted(nums)
        for i in range(len(num)):
            if i < len(num) - 1:
                res = abs(num[i] - num[i+1])
                if res > max_gap:
                    max_gap = res
        return abs(max_gap)
        