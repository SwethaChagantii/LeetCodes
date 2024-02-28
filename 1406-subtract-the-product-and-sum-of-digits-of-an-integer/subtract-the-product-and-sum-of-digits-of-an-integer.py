class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        prod = 1
        while(n>0):
            r = n % 10
            total = total + r
            prod  = prod * r
            n = n // 10
        return prod - total
        