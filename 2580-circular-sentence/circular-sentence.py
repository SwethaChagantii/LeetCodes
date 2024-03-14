class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        count = 0
        li = list(map(str,sentence.split(" ")))
        n = len(li)
        if len(li)>1:
            for i in range(len(li)): 
                if i+1 != len(li): 
                    if li[i][-1] == li[(i+1)%len(li)][0]:
                        count += 1
        if li[n-1][-1] == li[0][0]:
            count += 1
        if count == len(li):
            return True
        return False
        