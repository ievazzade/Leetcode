class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        
        if ROWS <= 2 or COLS <= 2:
            return
        
        def DFS(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 'O':
                board[row][col] = 'A'
                DFS(row - 1, col)
                DFS(row, col + 1)
                DFS(row + 1, col)
                DFS(row, col - 1)
                
        
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row == 0 or row == (ROWS - 1) or col == 0 or col == (COLS - 1)):
                    DFS(row, col)
                    
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O': board[row][col] = 'X'
                elif board[row][col] == 'A': board[row][col] = 'O'