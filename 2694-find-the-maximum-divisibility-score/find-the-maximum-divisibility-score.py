class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors = set(divisors)
        dic = {}
        li = []
        for num in nums:
            for div in divisors:
                if num % div == 0:
                    if div in dic:
                        dic[div] += 1
                    else:
                        dic[div] = 1
        
        if not dic:  
            return min(divisors)  
        
        max_value = max(dic.values())
        for key, value in dic.items():
            if value == max_value:
                li.append(key)
        return min(li)
