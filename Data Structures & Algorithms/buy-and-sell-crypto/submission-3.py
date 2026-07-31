class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use sliding window approach
        """
        1. Use two pointers, and have them start at 0th and 1th indecies.
        2. Always traverse second pointer
        3. If prices[idx_1] > prices[idx_2], set first idx = second idx.
        """
        max_profit = 0
        idx1 = 0
        idx2 = 0
        while idx2 < len(prices):
            max_profit = max(max_profit, prices[idx2] - prices[idx1])
            if prices[idx1] > prices[idx2]:
                idx1 = idx2
            idx2 += 1
            

        return max_profit