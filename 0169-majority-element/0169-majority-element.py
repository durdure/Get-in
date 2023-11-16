class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mode = 0
        freq = 1
        mf =0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                freq += 1
            else:
                if mf < freq:
                    mf = freq
                    mode = nums[i]
                    
                freq = 1 

        if mf < freq :
            mode = nums[len(nums)-1]       

        return mode 