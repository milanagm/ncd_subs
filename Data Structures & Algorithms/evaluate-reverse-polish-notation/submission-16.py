class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i.isalnum():
                stack.appen(i)
            else: 
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a+b)
                    continue
                if i == "-":
                    stack.append(a-b)
                    continue
                if i == "*":
                    stack.append(a*b)
                    continue
                if i == "/":
                    stack.append(a/b)
                    continue

        return stack[0]


