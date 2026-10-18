class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # wir haben 9 rows
        # wir haben 9 columns
        # und 9 boxes
        # meine idee: bedingungen checken und return False else True

        for row in board: 
            seen = set()
            for i in row: 
                if i == ".":
                    continue
                if i in seen: 
                    return False
                seen.add(i) 

        for i in range(0,9): 
            seen = set()
            for row in board: 
                if row[i] == ".":
                    continue
                if row[i] in seen: 
                    return False
                seen.add(row[i]) 
        
        return True
        
        




        