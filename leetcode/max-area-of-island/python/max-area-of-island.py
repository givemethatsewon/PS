class Solution(object):
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        areas = [0]

        def dfs(grid, r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0
            ): return 0
            
            # 방문 처리
            grid[r][c] = 0

            area = 1
            area += dfs(grid, r+1, c)
            area += dfs(grid, r-1, c)
            area += dfs(grid, r, c+1)
            area += dfs(grid, r, c-1)

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    areas.append(dfs(grid, i, j))


        return max(areas)
        

        