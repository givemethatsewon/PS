class Solution:
    def numIslands(self, grid):
        def dfsMark(graph, r, c):
            if min(r, c) < 0 or r == len(graph) or c == len(graph[0]) or graph[r][c] == "0":
                return  # base case
            if graph[r][c] == "1":
                graph[r][c] = "0"

            # 상하 좌우 탐색
            dfsMark(graph, r+1, c)
            dfsMark(graph, r-1, c)
            dfsMark(graph, r, c+1)
            dfsMark(graph, r, c-1)

        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for m in range(ROWS):
            for n in range(COLS):
                if grid[m][n] == "1":
                    dfsMark(grid, m, n)
                    count += 1
        return count
