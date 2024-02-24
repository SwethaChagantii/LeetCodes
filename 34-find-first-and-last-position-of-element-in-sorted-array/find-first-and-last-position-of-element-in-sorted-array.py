class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        li = []
        li2 = []
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                li.append(i)
        if len(li) > 2:
            li2 += [min(li),max(li)]
            li = li2
        if len(li) == 1:
            li.append(li[0])
        if target not in nums:
                li.append(-1)
                li.append(-1)
        return li
        