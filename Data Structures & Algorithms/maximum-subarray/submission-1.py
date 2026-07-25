class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force solution: iterating through all subarrays to get the max sum
        res = nums[0]
        for i in range(len(nums)): # i marks the start
            curr_res = 0
            for j in range(i, len(nums)): # j marks the end
                curr_res += nums[j]

                res = max(res, curr_res)
        return res