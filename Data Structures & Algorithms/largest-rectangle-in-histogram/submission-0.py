class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # храним индексы
        max_area = 0

        for i in range(len(heights)):
            # Pop пока текущий меньше вершины стека
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                # Ширина = расстояние между текущим и новой вершиной стека
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        # Обработать оставшиеся в стеке
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area