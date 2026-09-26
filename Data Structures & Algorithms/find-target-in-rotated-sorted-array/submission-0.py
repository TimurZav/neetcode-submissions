class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Левая половина отсортирована
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # левая половина отсортирована
                    # Лежит ли target в левой половине?
                    right = mid - 1 # ищем в левой
                else:
                    left = mid + 1 # ищем в правой
            # Правая половина отсортирована
            else:
                # Лежит ли target в правой половине?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 # ищем в правой
                else:
                    right = mid - 1 # ищем в левой
        return -1