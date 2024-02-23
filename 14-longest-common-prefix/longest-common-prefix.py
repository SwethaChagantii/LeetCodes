class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        s = ""
        n = len(arr)
        min_len = len(arr[0])
        for i in range(n):
            min_len = min(min_len,len(arr[i]))
        for j in range(min_len):
            common_char = arr[0][j]
            for i in range(1,n):
                if arr[i][j] != common_char:
                    return s
            s += arr[i][j]
        return s
            

        