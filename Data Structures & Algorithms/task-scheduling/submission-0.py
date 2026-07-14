import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)

        time = 0
        while heap:
            ran = 0
            temp = []
            for _ in range(n + 1):
                if heap:
                    c = heapq.heappop(heap)
                    ran += 1
                    if c + 1 < 0:
                        temp.append(c + 1)
            for c in temp:
                heapq.heappush(heap, c)
            time += (n + 1) if heap else ran
        return time