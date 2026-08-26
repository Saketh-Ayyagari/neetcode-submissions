class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # For the SMALLEST possible time, rate = max(piles) -> eating all piles in len(piles) hours.
        # LARGEST POSSIBLE TIME, rate = 1 -> eating all piles in sum(piles) hours. 
        # To find the number of hours it takes, the formula is
            # sum(ceiling(piles[i] / rate))

        """
        use binary search to search through the range [SMALLEST_RATE=1, LARGEST_RATE=max(piles)] to find the 
        smallest number of hours it takes
        """
        def calculateNumHours(rate: int) -> int:
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile / rate)
            return num_hours

        low = 1 # smallest possible rate
        high = max(piles) # largest possible rate
        res = -1

        while low <= high:
            mid_rate = (low + high) // 2
            num_hours = calculateNumHours(mid_rate)

            if num_hours > h:
                low = mid_rate + 1
            elif num_hours <= h:
                high = mid_rate - 1
                res = mid_rate

        return res                

        