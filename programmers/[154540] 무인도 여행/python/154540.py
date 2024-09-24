from typing import List
from collections import deque

def solution(maps: List[str]) -> List[int]:
    ROWS, COLS = len(maps), len(maps[0])
    grid = [list(row) for row in maps]
    visited = [[False]*COLS for _ in range(ROWS)]
    islands = []
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True
        total_food = int(grid[r][c])
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < ROWS and
                    0 <= ny < COLS and
                    not visited[nx][ny] and
                    grid[nx][ny] != 'X'
                ):
                    visited[nx][ny] = True
                    total_food += int(grid[nx][ny])
                    queue.append((nx, ny))
        return total_food
    
    for r in range(ROWS):
        for c in range(COLS):
            if not visited[r][c] and grid[r][c] != 'X':
                total_food = bfs(r, c)
                islands.append(total_food)
    
    return [-1] if not islands else sorted(islands)
