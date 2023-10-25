class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        if num1 < 0  and num2 < 0:
            return
    
        prod = num1*num2
        result = str(prod)
        return result