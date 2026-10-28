class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) -1 #anz zeilen!
        l_col, r_col = 0, len(matrix[0]) -1 #anz spalten!

        while l_row <= r_row:
            mid = (r_row - l_row) / 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                r_row = mid -1
            if target > matrix[mid][0]:
                l_row = mid + 1

        while l_col <= r_col: 
            mid = (r_col - l_col)/ 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                r_col = mid -1
            if target > matrix[mid][0]:
                l_col = mid + 1

        return False


        