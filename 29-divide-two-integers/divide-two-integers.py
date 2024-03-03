from math import ceil

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647 
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return int(dividend // divisor)
        else:
            return ceil(dividend / divisor)
