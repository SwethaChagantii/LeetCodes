class Solution:
    def trap(self, height: List[int]) -> int:
       
        n = len(height)
        lb = [0]*n
        rb = [0]*n
        lb[0] = height[0]
        for i in range(1,n):
            lb[i] = max(lb[i-1],height[i])
        rb[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            rb[i] = max(rb[i+1],height[i])
        res = 0
        for i in range(n):
            res += min(lb[i],rb[i]) - height[i]
        return res