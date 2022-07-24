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