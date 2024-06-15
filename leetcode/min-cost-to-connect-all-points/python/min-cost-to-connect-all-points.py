from heapq import *


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # asjacency list 형태로 그래프 나타내기
        points = [tuple(point) for point in points]
        adj = {point : [] for point in points}
        for other_point in points:
            for my_point in adj.keys():
                if my_point != other_point:
                    d = abs(my_point[0] - other_point[0]) + abs(my_point[1] - other_point[1])
                    adj[my_point].append([d, other_point])
        
        # adg => point : [cost, point, other_point]
        # visited 집합과 minHeap 초기화하기
        minHeap = []
        for d, other_point in adj[points[0]]:
            heappush(minHeap, [d, points[0], other_point])
        visited = set()
        visited.add(points[0])
        min_d = 0
        
        # 탐색
        n = len(points)
        while len(visited) < n:
            # print(visited, n, minHeap)
            d1, src1, dst1 = heappop(minHeap)
            
            if dst1 in visited:
                continue
            
            min_d += d1
            visited.add(dst1)
            
            src2 = dst1
            for d2, dst2 in adj[src2]:
                if dst2 not in visited:
                    heappush(minHeap, [d2, src2, dst2])
            
        return min_d

sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))