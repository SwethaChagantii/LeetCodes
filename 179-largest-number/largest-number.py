class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num==0 for num in nums):
            return "0"
        nums_str = [str(num) for num in nums]
        large = sorted(nums_str,key = lambda x:x*10,reverse=True)
        k = ''.join(large)
        return ''.join(large)

        