from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Step 1: Build the graph (Adjacency List)
        graph = defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1.0 / value  # Add reverse edge
        
        # Step 2: DFS function to find path product
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0  # One of the variables is not in graph
            
            if start == end:
                return 1.0  # a / a = 1.0
            
            visited.add(start)
            
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return result * weight
            
            return -1.0
        
        # Step 3: Process each query
        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))
        
        return results
