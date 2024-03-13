class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        li = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] != nums[j] :
                    if abs(nums[i]) == abs(nums[j]):
                        li.append(nums[i])
                        li.append(nums[j])
        if li:

            return max(li)
        return -1
        