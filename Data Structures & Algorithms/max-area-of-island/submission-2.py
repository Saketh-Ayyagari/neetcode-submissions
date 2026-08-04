class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Algorithm: use DFS from flood fill, but return the area of each island
        """
        # visited = [] # keeps track of all pairs (i, j) that are visited in the array 
        ROWS = len(grid)
        COLS = len(grid[0])
        # performs RECURSIVE DFS with the starting position being grid[i][j]. Returns the area of the island
        def dfs(i: int, j: int):
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0 # marks the island as visited, so we don't count the island's area again
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            
            

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: # this means either visited or empty (can be treated the same)
                    continue
                elif grid[i][j] == 1:
                    # perform dfs to mark other connected "1"s visited. Update the maximum area
                    max_area = max(dfs(i, j), max_area)
            

        return max_area