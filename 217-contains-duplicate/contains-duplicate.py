class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for ch in nums:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 0
        print(dic)
        for key,values in dic.items():
            if values >= 1:
                return True
        return False
        