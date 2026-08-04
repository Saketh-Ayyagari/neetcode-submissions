class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        Algorithm
        1. Perform DFS starting from image[sr][sc]
        2. Change the color of each neighbor from the original to "color" int
        '''
        ROWS = len(image)
        COLS = len(image[0])
        start = image[sr][sc]

        if color == start:
            return image
         
        # NOTE THIS IS RECURSIVE DFS
        def dfs(r, c):
            # base case: r >= ROWS, r < 0, c >= COLS, c < 0, (r, c) in visited -> terminate
            if (r >= ROWS or r < 0 or c >= COLS or c < 0 or image[r][c] != start):
                return
            # change image[sr][sc]
            image[r][c] = color
            # get neighbors of the specific node and call DFS on them as well
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image
             
            