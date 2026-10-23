class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        NEW ALGORITHM: 
        1. Get all sources/treasure chests and their locations (i, j).
        2. Add them ALL to a queue.
        3. Run multi-source BFS processing neighbors of each source. Also keep track of distances to some source, since nodes closer to one source will be processed FIRST
        """
        INF = (1 << 31) - 1
        M = len(grid)
        N = len(grid[0])

        # getting all sources
        sources = [(i, j) for i in range(M) for j in range(N) if grid[i][j] == 0]

        # adding to queue
        queue = deque()
        for (i, j) in sources:
            dist = 0
            queue.append((i, j, dist))
        
        visited = set()
        # starting BFS
        while queue:
            i, j, dist = queue.popleft()
            if (i >= 0 and i < M and j >= 0 and j < N) and (i, j) not in visited and grid[i][j] != -1: # (i, j) must be in range, (i, j) cannot be visited, AND grid[i][j] cannot be a water cell. 
                visited.add((i, j))
                grid[i][j] = dist # consider this like "processing a node"

                # neighbors
                NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for n in NEIGHBORS:
                    neighbor = (i + n[0], j + n[1], dist + 1)
                    queue.append(neighbor)
        

                
                    
