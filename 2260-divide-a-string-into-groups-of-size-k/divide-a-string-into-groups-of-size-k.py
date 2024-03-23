class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        li = []
        word = ""
        if len(s) % k != 0:
            rem = len(s) % k
            s += fill*(k-rem)
        for ch in s:
            word += ch
            if len(word) == k:
                li.append(word)
                word = ""
            
        return li
        