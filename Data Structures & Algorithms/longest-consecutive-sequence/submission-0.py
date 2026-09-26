class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        max_len = 0
        for num in set_nums:
            if num - 1 not in set_nums:   # начало последовательности
                length = 1
                while num + length in set_nums:
                    length += 1
                max_len = max(max_len, length)
        return max_len