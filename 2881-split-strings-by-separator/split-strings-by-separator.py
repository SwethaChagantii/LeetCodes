class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        li = []
        for word in words:
            result.append(word.split(separator))
        for ch in result:
            li.extend(filter(None,ch))
        return li
        


        