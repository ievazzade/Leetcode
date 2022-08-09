# Brute Force (Recursive)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid) - 1
        self.COLS = len(grid[0]) - 1
        return self.calculate(grid, 0, 0)
    
    def calculate(self, grid, row, col):
        if (row == self.ROWS) and (col == self.COLS):
            return grid[row][col]
        
        elif (row == self.ROWS) or (col == self.COLS):
            return grid[row][col] + (self.calculate(grid, row, col + 1) if (row == self.ROWS) else self.calculate(grid,row + 1, col))
        
        else:
            return grid[row][col] + min(self.calculate(grid, row + 1, col), self.calculate(grid, row, col + 1))


# Dynamic Programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        if  ROWS == 0:
            return 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row - 1) >= 0 and (col - 1) >= 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
                
                else:
                    if (row - 1) >= 0:
                        grid[row][col] += grid[row - 1][col]
                    elif (col - 1) >= 0:
                        grid[row][col] += grid[row][col - 1]
        
        return grid[ROWS - 1][COLS - 1]