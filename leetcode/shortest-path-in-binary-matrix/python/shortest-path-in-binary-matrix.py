from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 그래프 BFS 위한 설정
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        length = 1

        if grid[0][0] == 1:
            return -1
        queue.append((0, 0)) # 시작 위치
        visited.add((0, 0)) 
        

        # queue 기반 탐색 시작
        while queue: # 모두 비울때까지
            for i in range(len(queue)): # queue의 스냅샷
                r, c = queue.popleft()  # Vertex 꺼내기
                if  r == ROWS - 1 and c == COLS - 1 and grid[r][c] == 0:
                    return length   # 끝에 도착했는지 확인

                # 주변 탐색
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc
                    if (
                        min(next_r, next_c) < 0 or
                        next_r == ROWS or next_c == COLS or
                        (next_r, next_c) in visited or
                        grid[next_r][next_c] == 1
                    ): continue

                    # 유효한 좌표인 경우
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
            # queue 스냅샷 탐색 끝났으므로 다음 차례로
            length += 1
        
        return -1