class Solution(object):
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        r, c = ROWS - 1, COLS - 1
        islands = 0

        def dfs(grid, r, c):
            if (
                r == ROWS or c == COLS or
                min(r, c) < 0 or
                grid[r][c] == '0'
            ): return

            grid[r][c] = '0' # 방문 처리
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)
        

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    islands += 1
        
        return islands
        