class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i in "+,-,*, /":
                b = int(stack[-1])
                del stack[-1]
                a = int(stack[-1])
                del stack[-1]
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
        return int(stack[-1])
