class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # 과목별 선수 과목을 저장할 딕셔너리 초기화(인접 리스트 방식)
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # 현재 경로에 있는 과목들을 저장하는 집합 초기화
        visitSet = set()
        
        def dfs(crs):
            # base case: 순환 감지
            if crs in visitSet:
                return False
            # base case: 선수 과목이 없으면(그래프 끝에 도달하면) True 반환
            if preMap[crs] == []:
                return True
            
            # 현재 과목을 방문 집합에 추가
            visitSet.add(crs)
            # 선수 과목들에 대해 DFS 호출(자식들도 한 번씩 보내는 느낌)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            # DFS가 끝난 후 방문 집합에서 현재 과목 제거 및 preMap 업데이트
            visitSet.remove(crs)
            preMap[crs] = []  # 다음 호출 시 바로 True 반환되도록 설정
            
            return True
        
        # 모든 과목에 대해 DFS 수행하여 수강 가능 여부 판단
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
