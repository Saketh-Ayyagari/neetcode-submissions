class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # starting w/ first element, traverse w/ two pointers.
        """
        1. Traverse string w/ 2 pointers idx1 and idx2. Store recently seen characters in hashset
        2. If current 
        """
        longestLen = 0
        i = 0
        j = 0
        seen = set()
        while j < len(s):
            while s[j] in seen:
                longestLen = max(longestLen, len(seen))
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            j += 1
        longestLen = max(longestLen, len(seen))
        return longestLen