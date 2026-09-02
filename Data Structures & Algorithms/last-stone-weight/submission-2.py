class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): # reversing signs to turn into max heap
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            # first get the two largest stones (heap removal)
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if (x < y):
                heapq.heappush(stones, x - y)
            elif (x > y):
                heapq.heappush(stones, y - x)

        return 0 if len(stones) == 0 else -stones[0]