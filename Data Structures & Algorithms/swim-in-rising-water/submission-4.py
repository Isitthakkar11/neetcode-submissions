class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            cost, r, c = heapq.heappop(heap)

            if (r,c) == (n - 1, n - 1):
                return cost

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_cost = max(cost, grid[nr][nc])
                    heapq.heappush(heap, (new_cost, nr, nc))

        return -1