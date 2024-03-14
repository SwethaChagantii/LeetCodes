class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ""
        for ch in nums:
            s += str(ch)
        li = list(map(int,s))
        return li
        