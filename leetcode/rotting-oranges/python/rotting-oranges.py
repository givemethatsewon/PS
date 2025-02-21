class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        seconds = 0
        queue = deque()
        put = None

        # 썩은 바나나 좌표 삽입
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
        

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            put = False
            for i in range(len(queue)): # queue의 스냅샷 -> breadth 추적
                r, c = queue.popleft()                
                
                for dr, dc in directions:
                    nxt_r, nxt_c = r + dr, c+ dc
                    if (
                        min(nxt_r, nxt_c) < 0 or
                        nxt_r == ROWS or nxt_c == COLS or
                        grid[nxt_r][nxt_c] == 0 or grid[nxt_r][nxt_c] == 2
                    ): continue

                    put = True
                    queue.append((nxt_r, nxt_c))
                    grid[nxt_r][nxt_c] = 2
            
            if put:
                seconds += 1

        # 스캔        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return seconds
