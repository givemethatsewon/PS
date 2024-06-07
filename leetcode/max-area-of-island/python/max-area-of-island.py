class Solution:
    def maxAreaOfIsland(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(graph, r, c):
            if (
                    min(r, c) < 0 or
                    r == ROWS or c == COLS or
                    graph[r][c] == 0
            ):
                return 0

            # 마킹
            grid[r][c] = 0

            # size 계산
            size = 1
            size += dfs(graph, r + 1, c)
            size += dfs(graph, r - 1, c)
            size += dfs(graph, r, c + 1)
            size += dfs(graph, r, c - 1)

            return size

        maxSize = 0
        for m in range(ROWS):
            for n in range(COLS):
                if grid[m][n] == 1:
                    landSize = dfs(grid, m, n)
                    maxSize = max(landSize, maxSize)

        return maxSize