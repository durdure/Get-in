class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window  with O(n) notation
        # by brute force it become O(n^3)
        maxSub = nums[0]
        curSum = 0
        
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum+=i
            maxSub = max(maxSub, curSum)
        return maxSub
            