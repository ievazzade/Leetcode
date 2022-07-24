from numpy import diag


class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])

        result = []

        for d in range(m + n - 1):
            diagonal = []

            row = 0 if d < n else d - n + 1
            col = d if d < n else n - 1

            while row < m and col > -1:
                diagonal.append(mat[row][col])
                row += 1
                col -= 1
            
            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)

        return result

class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])

        result = []

        row, col = 0, 0
        direction = 1
        result = []
        
        while row < m and col < n:
            result.append(mat[row][col])
            
            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)
            
            if new_row < 0 or new_row == m or new_col < 0 or new_col == n:
                if direction:
                    row += (col == n - 1)
                    col += (col < n - 1)
                else:
                    col += (row == m - 1)
                    row += (row < m - 1)
                    
                direction = 1 - direction
            else:
                row = new_row
                col = new_col
        
        return result