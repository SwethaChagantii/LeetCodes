class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) == len(t):
            if list(s) == list(t):
                return True
        return False
        