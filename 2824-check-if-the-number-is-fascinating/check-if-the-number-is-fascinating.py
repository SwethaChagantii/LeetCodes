class Solution:
    def isFascinating(self, n: int) -> bool:
        li = ['1','2','3','4','5','6','7','8','9']
        n1 = 2*n
        n2 = 3*n
        s = str(n) + str(n1) + str(n2)
        if "0" not in s:
            if sorted(list(s)) == li:
                return True
        return False
        