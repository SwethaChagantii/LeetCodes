class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {"{":"}","(":")","[":"]"}
        for char in s:
            if char in braces:
                stack.append(char)
            elif stack and char == braces[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack

        