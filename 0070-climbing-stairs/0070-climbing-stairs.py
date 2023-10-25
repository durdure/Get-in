class Solution:
    def climbStairs(self, n: int) -> int:
        num, nums = 1, 1
        temp =0
        if n == 1:
            return 1
        for i in range(2, n+1):
            temp = num + nums
            num = nums
            nums = temp
        return temp