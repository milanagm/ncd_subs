class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i in "+,-,*, /":
                a = stack[-1]
                del stack[-1]
                b = stack[-2]
                del stack[-2]
                if i == "+": 
                    stack.append(a+b)
                if i == "-":
                    stack.append(a-b)
                if i == "*":
                    stack.append(a*b)
                if i == "/":
                    stack.append(a/b)
            else: 
                stack.append(i)
        return stack[-1]
