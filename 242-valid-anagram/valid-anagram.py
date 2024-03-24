class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li1 = list(map(str,s))
        li2 = list(map(str,t))
        if sorted(li1) == sorted(li2):
            return True
        return False
        