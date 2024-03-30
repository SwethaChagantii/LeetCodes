class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        count = 0
        n = len(nums)
        if n%2 == 0:
            for ch in nums:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
            for key,values in dic.items():
                if values % 2 == 0:
                    count += 1
            if count == len(dic):
                return True
        return False

        