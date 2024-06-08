from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1: return -1

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        valid_paths = list()
        
        # 탐색 초기 설정(초기 위치 방문 처리)
        queue.append((0, 0))
        visited.add((0, 0))
        length = 1
        
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)] 
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                if r == ROWS - 1 and c == COLS - 1:
                    valid_paths.append(length)
                    continue
            
                for dr, dc in directions:
                    offset_x, offset_y = r + dr, c + dc
                    if (
                        min(offset_x, offset_y) < 0 or  # out of bounds
                        offset_x == ROWS or offset_y == COLS or # out of bounds
                        grid[offset_x][offset_y] == 1 or    # 벽
                        (offset_x, offset_y) in visited
                    ):
                        continue
                    queue.append((offset_x, offset_y))
                    visited.add((offset_x, offset_y))
            length += 1
            
        return -1 if len(valid_paths) == 0 else min(valid_paths)