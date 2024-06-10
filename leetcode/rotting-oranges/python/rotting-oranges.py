from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque() # 현재 위치에서 방문 가능한 위치들 저장
        time = 0 # 시간 기록
        
        if not [num for row in grid for num in row if num == 1]:
            return time
        
        # 시작 점 찾기
        starting_points = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 2]        
        for start in starting_points:
            queue.append(start) # 시작점 큐에 삽입    
        
    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    off_r, off_c = r + dr, c + dc
                    if (
                        min(off_r, off_c) < 0 or
                        off_r == ROWS or off_c == COLS or
                        grid[off_r][off_c] == 0 or  # 빈 곳
                        grid[off_r][off_c] == 2     # 이미 썩은 오렌지
                    ):
                        continue
                    
                    # 주변에 썩지 않은 오렌지가 있는 경우
                    queue.append((off_r, off_c))
                    grid[off_r][off_c] = 2 # 썩은 오렌지로 마킹
            time += 1
            
        return -1 if [num for row in grid for num in row if num == 1] else time - 1
