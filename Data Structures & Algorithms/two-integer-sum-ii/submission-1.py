class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # {число: индекс}

        for i, num in enumerate(numbers):
            complement = target - num

            # Проверяем есть ли нужное число в словаре
            if complement in seen:
                return [complement, num]

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return []