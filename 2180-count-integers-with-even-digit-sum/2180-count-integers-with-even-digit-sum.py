class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(2,num+1):
            sum,j = 0,i
            while j != 0:
                d = j % 10
                sum = sum + d
                j = j // 10
            if sum % 2 == 0:
                count += 1
        return count
                