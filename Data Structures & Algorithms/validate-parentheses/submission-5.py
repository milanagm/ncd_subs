class Solution:
    def isValid(self, s: str) -> bool:
        #(([])[])
        stack = []

        for i,v in enumerate(s): 
            if v == "(":
                stack.append("(")
            if v == ")":
                if stack and stack[-1] == "(":
                    del stack[-1]
                else:
                    return False

            if v == "[":
                stack.append("[")
            if v == "]":
                if stack and stack[-1] == "[":
                    del stack[-1]
                else:
                    return False

            if v == "{":
                 stack.append("{")
            if v == "}":
                if stack and stack[-1] == "{":
                    del stack[-1]
                else:
                    return False
    
        return True