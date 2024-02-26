class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)
        for i in range(m,m+n):
            nums1[i] = nums2[k-n-i]
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if nums1[i] < nums1[j]:
                    temp = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = temp
        return nums1


        
        