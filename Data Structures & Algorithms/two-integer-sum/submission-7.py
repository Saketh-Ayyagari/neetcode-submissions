class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key: number, value: index
        for i in range(len(nums)):
            complement = target - nums[i] # first get complement
            if seen.get(complement) != None: # if complement in map, return both indecies
                return [seen[complement], i]
            else: # otherwise, add complement to the "seen" map (this ensures we can return indecies of DUPLICATE numbers)
                seen[nums[i]] = i
        return []