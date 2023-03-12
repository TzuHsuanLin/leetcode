class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tmp = str(bin(x ^ y))[2:]
        res = 0
        for i in range(len(tmp)):
            if tmp[i] == '1':
                res += 1
        return res
