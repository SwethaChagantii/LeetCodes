class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 <= x <= 2**31 - 1:
            if x < 0:
                rev_num = int(str(x)[1:][::-1])*-1
            else:
                rev_num = int(str(x)[::-1])
            if -2**31 <= rev_num <= 2**31 - 1:
                return rev_num
        return 0
        
        