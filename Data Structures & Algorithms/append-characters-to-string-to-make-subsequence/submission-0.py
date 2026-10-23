class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0 # going through s
        j = 0 # going through t

        while i < len(s):
            if j == len(t):
                break
            if s[i] == t[j]:
                j += 1
            i += 1
        
        ans = 0
        if j < len(t):
            ans = len(t) - j
        
        return ans
        