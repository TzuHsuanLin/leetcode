class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        res = 0
        while (i <= n):
            n -= i
            i += 1
            res += 1

        return res