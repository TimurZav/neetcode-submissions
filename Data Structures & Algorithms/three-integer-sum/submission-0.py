class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[left] + nums[i] + nums[right]
                if summ == 0:
                    result.add((nums[left], nums[i], nums[right]))
                    left += 1
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
        return [list(i) for i in result]