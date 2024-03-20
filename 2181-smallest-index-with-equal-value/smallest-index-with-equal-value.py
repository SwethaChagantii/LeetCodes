class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        dic = {key: None for key in nums}
        res = -1
        for i in range(len(nums)):
            print(i,i%10,nums[i])
            if i % 10 == nums[i]:
                res = i
                break
        return res
        