class Solution:
    def sumDigits(self,num):
        if num < 10:
            return num
        else:
            sum = 0
            while(num > 0):
                r = num % 10
                sum = sum + r
                num = num // 10
        if sum >= 10:
            return self.sumDigits(sum)
        return sum
    def addDigits(self, num: int) -> int:
        res = self.sumDigits(num)
        return res


        