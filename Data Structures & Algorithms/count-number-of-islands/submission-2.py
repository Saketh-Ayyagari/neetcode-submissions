class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = [] # keeps track of all pairs (i, j) that are visited in the array 
        ROWS = len(grid)
        COLS = len(grid[0])
        # performs ITERATIVE DFS with the starting position being grid[i][j] 
        def dfs(i: int, j: int):
            stack = [(i, j)]
            while stack:
                r, c = stack.pop()
                # proceeds to push neighbors if (r, c) is NOT visited
                if grid[r][c] != "0":
                    grid[r][c] = "0" # this marks the cell as visited
                    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                    neighbors = [(r, c) for r, c, in neighbors if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"]
                    for n in neighbors:
                        stack.append(n)
            

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