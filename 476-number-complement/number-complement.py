class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)
        bin_num = bin_num[2:]
        ch2 = ""
        for ch in bin_num:
            if ch == "1":
                ch2 += "0"
            else:
                ch2 += "1"
        return int(ch2,2)
        