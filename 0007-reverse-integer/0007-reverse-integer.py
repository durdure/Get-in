class Solution:
    def reverse(self, x: int) -> int:
        # by double slicing
        rev = 0
        max_int = 2 ** 31 -1
        min_int = -2 ** 31
        while (x != 0):
            digit = int(math.fmod(x, 10))
            if rev > max_int / 10 or rev < min_int / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            rev = rev * 10 + digit
            x = math.trunc(x / 10)
        return rev