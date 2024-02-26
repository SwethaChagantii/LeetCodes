class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        temp = nums
        flag = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if temp[i] < temp[j]:
                    flag = nums[i]
                    nums[i] = nums[j]
                    nums[j] = flag

