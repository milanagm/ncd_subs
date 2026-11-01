class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
       
        for i in tokens: 
            if i in "+-*/":
                b= int(result[-1])
                a= int(result[-2])
                del result[-1]
                del result[-1]
                if i == "+":
                    result.append(a+b)
                if i == "-":
                    result.append(a-b)
                if i == "*":
                    result.append(a*b)
                if i == "/":
                    result.append(a/b)
            else: 
                result.append(i)
        
        return int(result[-1])