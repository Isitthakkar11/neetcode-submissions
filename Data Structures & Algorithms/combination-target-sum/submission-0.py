class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def backtrack(start, total):
            if total == target:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    break
                path.append(nums[i])

                backtrack(i, total + nums[i])

                path.pop()

        backtrack(0, 0)
        return result