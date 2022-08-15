class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                prev_row, prev_col = row - 1, col - 1
                if 0 <= prev_row < ROWS and 0 <= prev_col < COLS:
                    if matrix[row][col] != matrix[prev_row][prev_col]:
                        return False
                    
        return True

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))