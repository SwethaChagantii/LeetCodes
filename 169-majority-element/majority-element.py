class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for ch in nums:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        max_freq = max(dic.values())
        for key in dic:
            if dic[key] == max_freq:
                return key

        