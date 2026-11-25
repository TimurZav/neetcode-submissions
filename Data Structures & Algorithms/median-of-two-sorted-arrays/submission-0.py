class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a

        total = len(a) + len(b)
        half = (total + 1) // 2
        left, right = 0, len(a)

        while left <= right:
            i = (left + right) // 2
            j = half - i

            a_left = a[i - 1] if i > 0 else float("-inf")
            a_right = a[i] if i < len(a) else float("inf")
            b_left = b[j - 1] if j > 0 else float("-inf")
            b_right = b[j] if j < len(b) else float("inf")

            if a_left > b_right:
                right = i - 1  # взяли слишком много из a
            elif b_left > a_right:
                left = i + 1   # взяли слишком мало из a
            else:
                left_max = max(a_left, b_left)
                if total % 2 == 1:
                    return float(left_max)

                right_min = min(a_right, b_right)
                return (left_max + right_min) / 2