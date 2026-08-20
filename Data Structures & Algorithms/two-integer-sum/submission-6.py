class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if seen.get(complement) != None:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i
        return []