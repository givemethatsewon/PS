class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
            

    def find(self, n):
        p = self.par[n]
        
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]] # 최적화 작업
            p = self.par[p]
        
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False    # 이미 union 되어 있으므로, 할 수 없음
        
        if self.rank[p1] > self.rank[p2]:   # 부모끼리 트리 높이 비교
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        total = len(edges)
            
        unioFind = UnionFind(total)
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            # 두 노드가 이미 연결되어 있다면 False 리턴
            if not unioFind.union(n1, n2):
                return edge