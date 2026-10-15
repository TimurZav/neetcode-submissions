class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        
        left, right = 0, len(numbers) - 1
    
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # 1-индексация
            elif total < target:
                left += 1
            else:
                right -= 1