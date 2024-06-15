class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {}
        for u, v in edges:
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
        
            graph[u].append(v)
            graph[v].append(u)
        
        for node in graph:
            if len(graph[node]) == len(edges): return node
            