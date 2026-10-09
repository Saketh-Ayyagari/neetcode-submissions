class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Algorithm
        
        1. For each node, perform a DFS if it has not been visited.
        2. If a node has been visited, then do not do anything.
        3. For each DFS, increment number of connected components by 1.
        """
 
        visited = set()
        def dfs(start: int):
            if start in visited:
                return
            # otherwise, mark current node as visited and look for neighbors
            visited.add(start)
            neighbors = set()
            for edge in edges:
                src, dest = edge
                if src == start:
                    neighbors.add(dest)
                elif dest == start:
                    neighbors.add(src)
            for n in neighbors:
                dfs(n)
        # go through all nodes

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
        