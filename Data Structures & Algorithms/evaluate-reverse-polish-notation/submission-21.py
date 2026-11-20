class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i not in {"+", "-", "*", "/"}:
                stack.append(i)
                print(stack)
                # 10 # 0  // # 6 # -132 // # 12 # -11 // # 9 # 3 
            else: 
                b = int(stack.pop()) # 3 # -11 # -132
                a = int(stack.pop()) # 9 # 12 # 6
                if i == "+":
                    stack.append(a+b) # 12
                    print(stack)
                    continue
                if i == "-":
                    stack.append(a-b)
                    print(stack)
                    continue
                if i == "*":
                    stack.append(a*b) # 12 * -11
                    print(stack)
                    continue
                if i == "/":
                    stack.append(a/b) # 6 / -132
                    print(stack)
                    continue

        return stack[0]