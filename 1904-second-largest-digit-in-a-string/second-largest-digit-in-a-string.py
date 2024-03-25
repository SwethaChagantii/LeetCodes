class Solution:
    def secondHighest(self, s: str) -> int:
        li = []
        for ch in s:
            if ch.isdigit() and int(ch) not in li:
                li.append(int(ch))
        li = sorted(li,reverse = True)
        print(li)
        if len(li) > 1:
            return li[1]
        return -1
        