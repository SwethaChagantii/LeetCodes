class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum = 0
        total = 0
        for i in range(1,n+1):
            if i % m == 0:
                sum = sum + i
            else:
                total = total + i
        return total-sum
        