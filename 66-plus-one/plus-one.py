class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        s_int = int(s) + 1
        s_str = str(s_int)
        li = []
        for i in range(len(s_str)):
            li.append(int(s_str[i]))
        return li
        