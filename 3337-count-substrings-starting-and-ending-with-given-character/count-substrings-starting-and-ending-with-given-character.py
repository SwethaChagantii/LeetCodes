class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        a_b = 0
        count = 0
        for i in range(len(s)):
            if s[i] == c:
                a_b += 1
                count += a_b
        return count
        

        