class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        li = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] != 1:
                li.append(count)
                count = 0
        li.append(count)
        return max(li)