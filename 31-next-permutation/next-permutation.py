from itertools import permutations
class Solution:
    @staticmethod
    def swap(nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]
        return nums
    def nextPermutation(self,nums):
        n = len(nums)
        i = n-2
        j = 0
        while i>=0:
            if nums[i] < nums[i+1]:
                break
            i = i-1
        if i<0:
            nums.reverse()
        else:
            for j in range(n-1,i,-1):
                if nums[j] > nums[i]:
                    break
            self.swap(nums,i,j)
            start,end = i+1,len(nums)
            nums[start:end] = nums[start:end][::-1]
        return nums




        
       
        