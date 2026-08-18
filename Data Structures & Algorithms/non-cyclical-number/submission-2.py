class Solution:
    def getSumSquaresOfDigits(self, num: int) -> int: # runs in O(log n)
        ans = 0
        while num > 0:
            digit = num % 10
            ans += digit * digit
            num = num // 10
        return ans

    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)

            n = self.getSumSquaresOfDigits(n)
            if n == 1:
                return True
            
        return False
            