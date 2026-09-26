class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)   # каждый элемент — подпоследовательность длиной 1
        for i in range(1, len(nums)):
            for j in range(0, i):       # смотрим все j перед i
                if nums[j] < nums[i]:                  # если можно продолжить
                    dp[i] = max(dp[i], dp[j] + 1)     # обновляем длину
        return max(dp)