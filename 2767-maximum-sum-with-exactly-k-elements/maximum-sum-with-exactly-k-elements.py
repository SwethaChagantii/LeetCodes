class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        max_ele = max(nums)
        for i in range(k):
            print(max_ele)
            total = total + max_ele
            max_ele += 1
        return total

        