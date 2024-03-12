class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n = len(words)
        count = 0
        if len(s) != n:
            return False
        for i in range(n):
            if words[i][0] == s[i]:
                count += 1
        if count == n:
            return True
        return False
        