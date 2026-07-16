class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                if not is_palindrome(start, i):
                    continue

                path.append(s[start:i + 1])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result
