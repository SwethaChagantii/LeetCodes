class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        for ch in nums:
            if ch in dic :
                dic[ch] += 1
            else:
                dic[ch] = 1
        sum = 0
        for key,value in dic.items():
            if value == 1:
                sum += key
        return sum