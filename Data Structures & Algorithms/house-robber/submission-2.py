class Solution:
    def rob(self, nums: List[int]) -> int:
        # RECURSIVE SOLUTION
        # def dfs(i: int, total: int):
        #     # base case: i >= len(nums) -> return total
        #     if i >= len(nums):
        #         return total
            
        #     return max(dfs(i + 2, total + nums[i]), dfs(i + 3, total + nums[i]))

        # return max(dfs(0, 0), dfs(1, 0))

        # DYNAMIC PROGRAMMING SOLUTION
        """
        Algorithm
        1. Go forwards to store cached results
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if (len(nums) > 1): # handles edge case where number of houses > 1
            dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)): # for cases where len(nums) > 2
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]
