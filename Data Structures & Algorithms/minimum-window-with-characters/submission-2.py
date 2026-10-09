class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        counter = Counter(t)
        window = Counter()
        have, need = 0, len(counter)
        left = 0
        res, res_len = (-1, -1), float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            if char in counter and window[char] == counter[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = (left, right)
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in counter and window[s[left]] < counter[s[left]]:
                    have -= 1
                left += 1

        return s[res[0]:res[1] + 1] if res_len != float("inf") else ""