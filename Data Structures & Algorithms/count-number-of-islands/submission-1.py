class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = [] # keeps track of all pairs (i, j) that are visited in the array 
        
        # performs RECURSIVE DFS with the starting position being grid[i][j] 
        def dfs(i: int, j: int):
            # base case: (i, j) is out of bounds, and grid[i][j] is already visited -> return
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == "0":
                return 
            grid[i][j] = "0" # this marks the cell as visited so we don't have to keep track of everything
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0": # this means either visited or empty (can be treated the same)
                    continue
                elif grid[i][j] == "1":
                    # perform dfs to mark other connected "1"s visited.
                    dfs(i, j)
                    num_islands += 1
            

        return num_islands