class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
       a =[]
       b =[]
       c = []
       d = []
       for i in range(len(arr1)):
        a.append((arr1[i]+arr2[i]+i))
        b.append(arr1[i]-arr2[i]+i)
        c.append(-arr1[i]+arr2[i]+i)
        d.append(-arr1[i]-arr2[i]+i)
       return max(max(a)-min(a),max(b)-min(b),max(c)-min(c),max(d)-min(d))