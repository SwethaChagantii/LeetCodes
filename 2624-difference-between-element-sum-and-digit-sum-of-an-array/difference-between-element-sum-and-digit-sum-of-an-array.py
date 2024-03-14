class Solution:
    def sum_digit(self,num):
        tot1 = 0
        while(num != 0):
            rem = num % 10
            tot1 += rem
            num //= 10
        return tot1
    def differenceOfSum(self, nums: List[int]) -> int:
        tot1 = 0
        for num in nums:
            tot1 += self.sum_digit(num)
        
        
        tot2 = sum(nums)
        print(tot1,tot2)

        return abs(tot2-tot1)
        