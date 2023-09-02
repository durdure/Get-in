class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This is the two pointer question there is must be 
        # use empty list as learned i stack
        # which can help us to store all element in box by order
        res = []
        nums.sort()
        length = len(nums)
        # sort the give list
        
        
        #             by using two pointer
        
        #    left and rigth form the start and the end of the list
        for i in range(length-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = length -1
            
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result < 0:
                    left = left + 1
                  
                elif result > 0:
                     right = right -1
                else:
                    # by using append() function for selection of the element
                    res.append([nums[i], nums[left], nums[right]])
                # to avoid the duplication of the element                     
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right-1]:
                        right = right -1
                        
                        
                    left = left + 1
                    right = right -1
        return res
                    