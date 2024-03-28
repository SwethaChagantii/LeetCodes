class Solution:
    def maxPower(self, s: str) -> int:
      max_pow = 1
      cur_pow = 1
      for i in range(1,len(s)):
        if ord(s[i-1]) == ord(s[i]):
            cur_pow += 1
        else:
            max_pow = max(max_pow,cur_pow)
            cur_pow = 1
      return max(max_pow,cur_pow)
           
        