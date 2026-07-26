class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(step):
            if step <= 2:
                return step
            if step in memo:
                return memo[step]
            memo[step] = ways(step - 1) + ways(step - 2)
            return memo[step]
        return ways(n)