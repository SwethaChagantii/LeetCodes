class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        li = []
        dic = {}
        for ch in arr:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        occurrences = list(dic.values())
        return len(occurrences) == len(set(occurrences))