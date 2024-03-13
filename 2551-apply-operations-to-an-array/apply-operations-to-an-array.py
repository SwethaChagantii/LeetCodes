class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        li = []
        li2 = []
        for i in range(len(nums)):
            if i+1 != len(nums):
                if nums[i] == nums[i+1]:
                    nums[i] = nums[i]*2
                    nums[i+1] = 0
        for ch in nums:
            if ch != 0:
                li.append(ch)
        for ch in nums:
            if ch == 0:
                li.append(ch)

        return li

        