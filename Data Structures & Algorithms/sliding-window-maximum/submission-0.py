class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # хранит индексы
        left = 0

        for right in range(len(nums)):
            # убираем из конца все элементы меньше текущего
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            # убираем из начала если вышел за окно
            if dq[0] < left:
                dq.popleft()

            # начинаем добавлять результат когда окно заполнено
            if right >= k - 1:
                result.append(nums[dq[0]])
                left += 1

        return result