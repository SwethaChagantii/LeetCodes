class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        li = []
        for i in range(len(arr)):
            if arr[i] == 0:
                if len(li) < len(arr):
                    li.append(0)
                    li.append(0)
            else:
                li.append(arr[i])
        for i in range(len(arr)):
            arr[i] = li[i]
        return arr
        