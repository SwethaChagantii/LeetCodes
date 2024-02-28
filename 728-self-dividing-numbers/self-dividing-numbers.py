class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li = []
        for i in range(left,right+1):
            if i % 10 != 0:
                temp = i
                count = 0
                l = len(str(i))
                for ch in str(i):
                    if int(ch) != 0:
                        if temp % int(ch) == 0:
                            count += 1
                if count == l:
                    li.append(i)
        return li




        