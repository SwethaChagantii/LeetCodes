class Solution:
    def convertToTitle(self, colNum: int) -> str:
        result = ""
        while colNum > 0:
            colNum -= 1
            rem = colNum % 26
            result =  chr(65 + rem) + result
            colNum //= 26
        return result
        