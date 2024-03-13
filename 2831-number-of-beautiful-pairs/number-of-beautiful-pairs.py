class Solution:
    def gcd(num1,num2):
        while num2:
            num1,num2 = num2,num1%num2
        return num1
            
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        nums = list(map(str,nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if gcd(int(nums[i][0]),int(nums[j][-1])) == 1:
                    print(nums[i],nums[j])
                    count += 1
        return count

        