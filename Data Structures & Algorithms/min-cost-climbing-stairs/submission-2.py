class Solution:
    # recursive helper function
    def minCostClimbingStairsHelper(self, cost: List[int], step: int, curr_cost: int) -> int:
        # base case: reached the final step -> return the cost
        if step >= len(cost):
            return curr_cost
        curr_cost += cost[step]
        return min(self.minCostClimbingStairsHelper(cost=cost, step=step + 1, curr_cost=curr_cost), self.minCostClimbingStairsHelper(cost, step + 2, curr_cost))
            
            
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cache the results of the number of steps in an array.
        res = [0] * (len(cost) + 1)
        # initializing results of first 2 elements

        for i in range(2, len(res)):
            res[i] = min(res[i - 1] + cost[i - 1], res[i - 2] + cost[i - 2]) # the minimum cost to go up to step "i"
        return res[len(cost)]
        