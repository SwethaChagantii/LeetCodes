class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        li = []
        for word in strs:
            if word.isdigit():
                li.append(int(word))
            else:
                li.append(len(word))
        max_len = 0
        for word in li:
            max_len = max(word,max_len)
        return max_len

        