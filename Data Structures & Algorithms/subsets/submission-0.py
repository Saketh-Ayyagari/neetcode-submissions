class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        s = []
        def dfs(i: int):
            # base case: index == len(nums)
            if i == len(nums):
                subsets.append(s.copy())
            else:
                s.append(nums[i])
                dfs(i + 1)
                s.remove(nums[i])
                dfs(i + 1)

        dfs(0)

        return subsets