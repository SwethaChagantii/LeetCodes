from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = []
        m = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            m[sorted_s].append(s)
        
        for value in m.values():
            res.append(value)
        
        return res
