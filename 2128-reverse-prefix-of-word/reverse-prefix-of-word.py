class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = ""
        right = ""
        for i in range(len(word)):
            if word[i] == ch:
                left = word[:i+1]
                right = word[i+1:]
                break
        left = left[::-1]
        if ch not in word:
            return word
        return left+right
        