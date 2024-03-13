class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        li = []
        li.append(0)  

        for ch in nums:
            li.append(ch)
        for i in range(1,len(li)):
            if n % i == 0:
                total = total + li[i]*li[i]
        return total




        