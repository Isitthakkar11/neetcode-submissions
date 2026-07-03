class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum(math.ceil(pile / k) for pile in piles)

        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2

            if hours_needed(mid) <= h:
                result = mid
                right = mid - 1

            else:
                left = mid + 1

        return result
