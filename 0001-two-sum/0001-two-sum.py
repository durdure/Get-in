class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Double for-loop by boute force : time and space complecity O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        #by using the dictionary O(n) notation
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            elif num not in dic:
                dic[num]=i