class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for step in range(len(nums)):
            min_indx = step
            for i in range(step+1, len(nums)):
                if nums[i] < nums[min_indx]:
                    min_indx = i
            nums[step], nums[min_indx] = nums[min_indx], nums[step]
            