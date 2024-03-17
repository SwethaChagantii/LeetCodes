class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        m = len(nums[0])
        n = len(nums)
        dic = {}
        for i in range(n):
            m = len(nums[i])
            for j in range(m):
                if nums[i][j] in dic:
                    dic[nums[i][j]] += 1
                else:
                    dic[nums[i][j]] = 1
        li = []
        for key,values in dic.items():
            if values == n:
                li.append(key)
        return sorted(li)


        