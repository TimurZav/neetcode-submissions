class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # {число: индекс}

        for i, num in enumerate(numbers):
            complement = target - num

            # Проверяем есть ли нужное число в словаре
            if complement in seen:
                return [complement, num]

            # Сохраняем текущее число и его индекс
            seen[num] = i

        return []  # Если решения нет