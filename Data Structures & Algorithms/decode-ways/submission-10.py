class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(2, len(s) + 1):
            current = 0

            if s[i - 1] != '0':
                current += prev1

            two_digits = int(s[i - 2: i])
            if 10 <= two_digits <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1