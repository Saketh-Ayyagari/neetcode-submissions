class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # base case: m = 1, n = 1 -> return 1
        # if m == 1 and n == 1: # if we reach target spot, return 1
        #     return 1
        # if m < 0 or n < 0: # terminating condition if m or n go out of bounds
        #     return 0
        # return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        
        # WITH DYNAMIC PROGRAMMING
        dp = [[0] * n] * m # first initialize 2d DP
        dp[0] = [1] * n
        for i in range(1, m):
            dp[i][0] = 1
         
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]