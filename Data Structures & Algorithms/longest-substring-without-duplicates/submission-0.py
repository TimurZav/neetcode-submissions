class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        max_length = 0
        window = set()

        for right in range(len(s)):
            # Сжимаем окно пока есть дубликат
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # Добавляем текущий символ
            window.add(s[right])

            # Обновляем максимум
            max_length = max(max_length, right - left + 1)

        return max_length