class Solution:
    def isValid(self, s: str) -> bool:
        #(([])[])
        open_plain = []
        open_fancy = []
        open_squared = []

        for i,v in enumerate(s): 
            if v == "(":
                open_plain.append("(")
            if v == ")":
                if open_plain and open_plain[-1] == "(":
                    del open_plain[-1]
                else:
                    open_plain.append(")")

            if v == "[":
                open_fancy.append("[")
            if v == "]":
                if open_fancy and open_fancy[-1] == "[":
                    del open_fancy[-1]
                else:
                    open_fancy.append("]")

            if v == "{":
                 open_squared.append("{")
            if v == "}":
                if open_squared[-1] == "{":
                    del open_squared[-1]
                else:
                    open_squared.append("}")
            
        if len(open_plain) != 0: 
            return False
        if len(open_fancy) != 0: 
            return False
        if len(open_squared) != 0: 
            return False
    
        return True