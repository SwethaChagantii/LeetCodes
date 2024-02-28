class Solution:
    def findGCD(self, nums: List[int]) -> int:
        if all(nums) == nums[0]:
            max_ele = min_ele = nums[0]
        else:
            max_ele = max(nums)
            min_ele = min(nums)
        div  = []
        for i in range(1,max_ele+1):
            if max_ele % i == 0 and min_ele % i == 0:
                div.append(i)
        return max(div)
        