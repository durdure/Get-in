class Solution:
    def arrangeCoins(self, n: int) -> int:
        l , r = 0, n
        result = 0
        while l <= r:
            mid = (l + r) // 2
            coin = (mid / 2) * (mid+1)
            if coin > n:
                r = mid - 1
            else:
                l = mid+1
                result = max(mid,result)
        return result