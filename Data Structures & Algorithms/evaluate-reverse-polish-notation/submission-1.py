class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
       
        for i in tokens: 
            if i in "+-*":
                a= result[-1]
                b= result[-2]
                if i == "+":
                    result.append(a+b)
                if i == "-":
                    result.append(a-b)
                if i == "*":
                    result.append(a*b)
            else: 
                result.append(i)
        
        return result
            