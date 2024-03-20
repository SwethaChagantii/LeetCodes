class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        dic = {key: None for key in nums}
        li = []
        for i in range(len(nums)):
            print(i%10,nums[i])
            if i % 10 == nums[i]:
                li.append(nums[i])
                dic[nums[i]] = i
                break
        print(dic)
        if li:
            min_ele = min(li)
            for key,value in dic.items():
                if key == min_ele:
                    return value
        return -1

        