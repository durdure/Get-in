class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
            
        for indx, j in enumerate(nums):
            right_sum -= j
            if left_sum == right_sum:
                return indx
            left_sum += j
        return -1