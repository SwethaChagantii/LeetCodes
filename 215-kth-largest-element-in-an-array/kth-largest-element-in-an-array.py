class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        li = sorted(nums,reverse = True)
        return li[k-1]
        