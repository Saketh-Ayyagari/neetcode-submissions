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
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2, len(res)):
            additional = 0 if i == len(res) - 1 else cost[i]
            res[i] = min(res[i - 1] + additional, res[i - 2] + additional) # the minimum cost to go up to step "i"
        return res[len(cost)]
        