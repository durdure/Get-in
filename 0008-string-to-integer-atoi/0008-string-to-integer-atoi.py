class Solution:
    def myAtoi(self, s: str) -> int:
        mi = -2**31
        ma = 2**31-1
        b= 1
        n = 0
        empty = True
        for c in s:
            if empty:
                if c == " ":
                    continue
                elif c == "+":
                    b = 1
                elif c == "-":
                    b = -1
                elif c.isdigit():
                    n = int(c)
                else:
                    return 0
                empty = False
            else:
                if c.isdigit():
                    n = n*10 + int(c)
                    if b*n > ma: return ma
                    elif b*n < mi: return mi
                else:
                    break
        return b*n
        
        