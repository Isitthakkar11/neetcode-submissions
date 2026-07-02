class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

        if window_count == s1_count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            left += 1

            if window_count == s1_count:
                return True

        return False





