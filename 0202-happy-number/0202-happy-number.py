class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        
        while n!=1 and n not in num:
            num.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1