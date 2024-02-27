class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok = {"+","*","-","/"}
        stack = []
        n = len(tokens)
        for i in range(0,n):
            if tokens[i] not in tok:
                stack.append(int(tokens[i]))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if tokens[i] == "+":
                    res = operand1 + operand2
                    stack.append(res)
                elif tokens[i] == "-":
                    res = operand2 - operand1
                    stack.append(res)
                elif tokens[i] == "*":
                    res = operand1 * operand2
                    stack.append(res)
                elif tokens[i] == "/":
                    res = operand2 / operand1
                    stack.append(int(res))
        return stack[0]