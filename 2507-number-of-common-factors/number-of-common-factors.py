class Solution:
    def factors(self,num):
        li = []
        for i in range(1,num+1):
            if num % i == 0:
                li.append(i)
        return li
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        li1 = self.factors(a)
        li2 = self.factors(b)
        for ch in li1:
            if ch in li2:
                count += 1
        return count
        