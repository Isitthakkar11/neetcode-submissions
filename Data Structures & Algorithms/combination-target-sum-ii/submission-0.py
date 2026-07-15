class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start, total):
            if total == target:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])

                backtrack(i + 1, total + candidates[i])

                path.pop()

        backtrack(0, 0)
        return result