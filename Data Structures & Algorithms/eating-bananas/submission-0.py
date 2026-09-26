class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / mid) for pile in piles)
                
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left