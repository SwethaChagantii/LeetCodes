class Solution:
    def checkString(self, s: str) -> bool:
        s2 = ""
        s3 = ""
        for ch in s:
            if ch == 'a':
                s2 += ch
            elif ch == 'b':
                s3 += ch
        tot = s2 + s3
        if tot == s:
            return True
        return False

        