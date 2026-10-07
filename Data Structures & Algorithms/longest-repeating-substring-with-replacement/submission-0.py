class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        left = 0
        max_length = float("-inf")
        max_freq = 0  # макс. частота любого символа в окне
        count = {}    # частота символов в окне

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # если окно невалидно — сдвигаем left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        return max_length