class Solution:
    def maximumWealth(self, arr: List[List[int]]) -> int:
        n = len(arr)
        li = []
        for i in range(n):
            sum = 0
            for j in range(len(arr[i])):
                sum = sum + arr[i][j]
                li.append(sum)
        return max(li)

        