class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # wir haben 9 rows
        # wir haben 9 columns
        # und 9 boxes
        # meine idee: bedingungen checken und return False else True

        for row in board: 
            seen = {}
            for i in row: 
                if i in seen: 
                    return False
                seen.add(i) # ich glaube falsche syntax



        