class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) -1 #anz zeilen!
        l_col, r_col = 0, len(matrix[0]) -1 #anz spalten!

        while l_row <= r_row:
            mid = (l_row - r_row) / 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                mid -= 1
            if target > matrix[mid][0]:
                mid += 1

        while l_col <= r_col: 
            mid = (l_col - r_col)/ 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                mid -= 1
            if target > matrix[mid][0]:
                mid += 1
            
        return False


        