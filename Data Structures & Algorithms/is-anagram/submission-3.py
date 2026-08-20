class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort both strings and see if they are equal
        return sorted(s) == sorted(t)