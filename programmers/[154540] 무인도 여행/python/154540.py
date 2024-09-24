from typing import List

def solution(maps: List[str]) -> List[int]:
    ROWS, COLS = len(maps), len(maps[0])
    grid = [list(row) for row in maps]
    visited = [[False]*COLS for _ in range(ROWS)]
    islands = []
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def dfs_iterative(r, c):
        stack = [(r, c)]
        total_food = 0
        
        while stack:
            x, y = stack.pop()
            if (
                0 <= x < ROWS and
                0 <= y < COLS and
                not visited[x][y] and
                grid[x][y] != 'X'
            ):
                visited[x][y] = True
                total_food += int(grid[x][y])
                for dx, dy in directions:
                    stack.append((x + dx, y + dy))
        return total_food
    
    for r in range(ROWS):
        for c in range(COLS):
            if not visited[r][c] and grid[r][c] != 'X':
                total_food = dfs_iterative(r, c)
                islands.append(total_food)
                    
    return [-1] if not islands else sorted(islands)
