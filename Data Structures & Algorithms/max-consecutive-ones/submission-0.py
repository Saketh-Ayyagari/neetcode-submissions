class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num_ones = 0
        curr_num_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_num_ones += 1
            else:
                max_num_ones = max(max_num_ones, curr_num_ones)
                curr_num_ones = 0
        return max(max_num_ones, curr_num_ones)