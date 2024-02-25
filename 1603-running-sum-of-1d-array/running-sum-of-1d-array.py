class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        n = len(nums)
        li = []
        for i in range(n):
            sum = sum + nums[i]
            li.append(sum)
        return li

        