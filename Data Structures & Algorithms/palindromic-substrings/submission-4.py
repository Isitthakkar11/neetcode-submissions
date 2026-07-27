class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            total += expand(i, i)
            total += expand(i, i + 1)

        return total
        