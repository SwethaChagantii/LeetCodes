class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        li = []
        for word in sentences :
            count = 0
            for ch in word:
                if ch == " ":
                    count += 1
            li.append(count)
        return max(li) + 1


        