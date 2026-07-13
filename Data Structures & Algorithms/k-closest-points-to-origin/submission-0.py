class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x * x + y * y
            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y))
            elif -dist > heap[0][0]:
                heapq.heapreplace(heap, (-dist, x, y))

        return [[x, y] for (_, x, y) in heap]
        
