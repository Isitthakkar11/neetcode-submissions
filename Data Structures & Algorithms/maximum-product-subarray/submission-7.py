class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp_max = max(n, n * max_prod, n * min_prod)
            min_prod = min(n, n * max_prod, n * min_prod)
            max_prod = temp_max

            result = max(result, max_prod)
        return result