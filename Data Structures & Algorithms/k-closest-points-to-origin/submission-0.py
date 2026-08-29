class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first get distances to each point (their SQUARES)
        distances = []
        for i in range(len(points)):
            x, y = points[i]
            distances.append(math.sqrt(x * x + y * y))
        # now store each one in a heap
        heap = []
        for i in range(len(points)):
            heap.append((distances[i], points[i]))

        heapq.heapify(heap)
        res = []
        for _ in range(k):
            __, point = heapq.heappop(heap)
            res.append(point)
        
        return res

