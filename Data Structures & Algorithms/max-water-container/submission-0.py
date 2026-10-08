class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Вычисляем площадь для текущей пары линий
            width = right - left
            current_height = min(height[left], height[right])
            area = current_height * width

            # Обновляем максимум
            max_water = max(max_water, area)

            # Жадный выбор: двигаем указатель с меньшей высотой
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water