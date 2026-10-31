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
                if open_plain[-1] == "(":
                    del open_plain[-1]

            if v == "[":
                open_plain.append("[")
            if v == "]":
                if open_plain[-1] == "[":
                    del open_plain[-1]

            if v == "{":
                 open_plain.append("{")
            if v == "}":
                 if open_plain[-1] == "{":
                    del open_plain[-1]
            
        if len(open_plain) != 0: 
            return False
        if len(open_fancy) != 0: 
            return False
        if len(open_squared) != 0: 
            return False
    
        return True