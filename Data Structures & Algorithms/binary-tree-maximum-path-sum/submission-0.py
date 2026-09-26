# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            """
            Рекурсивная функция возвращает максимум ОДНОГО пути от node вниз.
            Попутно обновляет глобальный max_sum, учитывая "перевёрнутую V".
            """
            nonlocal max_sum

            # Базовый случай: пустой узел не даёт суммы
            if not node:
                return 0

            # Рекурсивно находим макс пути в левом и правом поддереве
            # max(0, ...) означает: если ветка отрицательная, НЕ БЕРЁМ её (=0)
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            # ВАЖНО! Обновляем глобальный максимум
            # Путь "перевёрнутая V": левая ветка + node + правая ветка
            max_sum = max(max_sum, node.val + left_max + right_max)

            # Возвращаем родителю: node + ОДНА ветка (левая ИЛИ правая)
            # Родитель не может использовать обе ветки одновременно!
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_sum # type:ignore