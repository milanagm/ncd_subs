class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up_row, down_row = 0, len(matrix) - 1
        l_col, r_col = 0, len(matrix[0]) - 1

        row = 0
        while up_row <= down_row:
            row = up_row + (down_row - up_row) // 2
            if target < matrix[row][0] :
                down_row = row - 1
            elif target > matrix[row][0] and target < matrix[row][len(matrix[0])-1] : 
                up_row = row + 1
            else: 
                break 
        
        col = 0
        while l_col <= r_col: 
            col = l_col + (l_col + r_col) // 2
            if target == matrix[row][col]: 
                return True
            if target < matrix[row][col]:
                r_col = r_col - 1
            elif target > matrix[row][col]: 
                l_col = l_col + 1
            else: 
                return False 
        
        


        
        
       