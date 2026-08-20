class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for num in nums: # loops through all numbers
            if s.get(num) == 1: # gets the value given the specific key
                return True
            s[num] = 1 # if key doesn't exist, then assign some value to it
        return False