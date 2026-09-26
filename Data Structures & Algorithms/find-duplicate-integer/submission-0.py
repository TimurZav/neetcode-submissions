class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]          # Черепаха делает 1 шаг
            fast = nums[nums[fast]]    # Заяц делает 2 шага
            
        # Фаза 2: Поиск входа в цикл (это и есть дубликат).
        # Возвращаем одного указателя в самое начало (индекс 0).
        slow = 0
        while slow != fast:
            slow = nums[slow]          # Теперь оба делают строго по 1 шагу
            fast = nums[fast]
            
        return slow