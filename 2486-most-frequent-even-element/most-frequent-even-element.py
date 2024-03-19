class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        for ch in nums:
            if ch % 2 == 0:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
        print(dic)
        li = []
        max_val = 0
        for key,values in dic.items():
            if values >= max_val:
                max_val = values
        for key,values in dic.items():
            if values == max_val:
                li.append(key)
        print(li)
        if li:
            return min(li)
        return -1
        
        