class Solution:
    def networkDelayTime(self, times, n, k):
        adj = {}  # 각 노드의 인접 리스트 기록 => 그래프 표현
        for i in range(1, n+1):
            adj[i] = []  # 인접 리스트 초기화
        
        # 인접 리스트에 값 넣기
        for src, dst, time in times:  # src, dst, time
            adj[src].append((dst, time))  # dst와 time을 묶어서 삽입(꺼낼때로 같이)
            
        # 최소 시간 기록할 해시맵
        minTime = {}
        minHeap = [(0, k)]  # 정렬 이슈때문에 time, destination 순으로 튜플 삽입

        while minHeap:
            time1, dst1 = heappop(minHeap)
            if dst1 in minTime:
                continue  # 이미 방문한 노드는 건너뜀
            
            minTime[dst1] = time1  # 현재 노드까지의 도착 시간을 갱신
            
            for dst2, time2 in adj[dst1]:
                if dst2 not in minTime:
                    heappush(minHeap, (time1 + time2, dst2))  # 다음 노드와 누적 시간을 최소 힙에 삽입
        
        if len(minTime) != n:
            return -1  # 모든 노드를 방문하지 못한 경우
        
        # 모든 노드를 방문한 경우, 가장 큰 도착 시간을 반환
        return max(minTime.values())
