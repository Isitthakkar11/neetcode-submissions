class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                current = max(money + prev2, prev1)
                prev2 = prev1
                prev1 = current
            return prev1

        exclude_first = rob_line(nums[1:])
        exclude_last = rob_line(nums[:-1])
        return max(exclude_first, exclude_last)