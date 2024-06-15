class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {i : [] for i in range(1, len(edges) + 2)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for node in graph:
            if len(graph[node]) == len(edges): return node
            