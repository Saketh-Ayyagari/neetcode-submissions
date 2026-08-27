import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first get frequency map
        freq_map = {}
        for num in nums:
            if freq_map.get(num):
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # then store frequency pairs in a max heap using heapq
        heap = []
        for key in freq_map:
            heap.append((-freq_map[key], key))
        """
        NOTE: For best compatability, we are only using min-heaps instead of max-heaps. Therefore, to
        get the "max-heap" functionality out the min-heap, we must revert the main values being compared.
        """
        heapq.heapify(heap) # order the heap based on the frequencies. 
        
        # now pop from the heap k times and store integers in a list
        res = []
        for _ in range(k):
            __, num = heapq.heappop(heap)
            res.append(num)
        return res
        
