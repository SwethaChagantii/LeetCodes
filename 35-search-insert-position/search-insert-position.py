class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)
            return self.searchInsert(nums,target)
        