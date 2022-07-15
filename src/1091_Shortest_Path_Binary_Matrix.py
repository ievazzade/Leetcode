class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1),(1,-1), (1, 0), (1, 1)]
        
        def get_neighbors(row, col):
            for row_diff, col_diff in directions:
                r, c = row + row_diff, col + col_diff
                if not (0 <= r <= max_row and 0 <= c <= max_col):
                    continue
                if grid[r][c] != 0:
                    continue
                yield (r, c)
        
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1
                queue.append((neighbor_row, neighbor_col))
        
        return -1


class Solution:
    def shortestPathBinaryMarix(grid):
        max_row = len(grid) - 1 
        max_col = len(grid[0]) - 1
        directions = [(-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1), (1,-1), (1,0), (1,1)]

        def get_neighbors(row, col):
            for row_offset, col_offset in directions:
                r, c = row + row_offset, col + col_offset
                if not (0 <= r <= max_row and 0 <= c <= max_col):
                    continue
                if grid[r][c] != 0:
                    continue

                yield (r, c)

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque((0,0,1))
        visited = {(0,0)}

        while queue:
            row, col, distance= queue.popleft()
            if (row, col) == (max_row, max_col):
                return distance
            for neighbor in get_neighbors(row, col):
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append((*neighbor, distance + 1))

        return -1