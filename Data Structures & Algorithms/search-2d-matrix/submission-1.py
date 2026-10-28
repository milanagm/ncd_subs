class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) #anz zeilen!
        l_col, r_col = 0, len(matrix[0]) -1 #anz spalten!

        while l_row <= r_row:
            mid = len(matrix) / 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                mid -= 1
            if target > matrix[mid][0]:
                mid += 1

        while l_col <= r_col: 
            mid = len(matrix[0]) / 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                mid -= 1
            if target > matrix[mid][0]:
                mid += 1
            
        return False


        