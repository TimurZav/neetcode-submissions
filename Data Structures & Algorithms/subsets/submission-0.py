class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
    
        def backtrack(start, path):
            result.append(path[:])       # сохраняем копию текущего пути
            for i in range(start, len(nums)):
                path.append(nums[i])     # делаем выбор
                backtrack(i + 1, path)   # рекурсия с следующей позиции
                path.pop()               # откат

        backtrack(0, [])
        return result