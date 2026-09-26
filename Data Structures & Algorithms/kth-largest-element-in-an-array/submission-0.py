class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            # Если куча больше k, выталкиваем минимум
            if len(heap) > k:
                heapq.heappop(heap)

        # Корень кучи = k-й наибольший
        return heap[0]