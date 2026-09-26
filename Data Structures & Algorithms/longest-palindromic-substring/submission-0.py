class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        best = ""
        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > len(best):
                best = odd

            even = expand(i, i + 1)
            if len(even) > len(best):
                best = even

        return best