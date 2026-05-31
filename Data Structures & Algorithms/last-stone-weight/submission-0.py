class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap)>=2:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            res = -(s1-s2)
            heapq.heappush(heap,res)
        
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
        