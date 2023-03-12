class Solution:
    def addDigits(self, num: int) -> int:
        nums = [int(a) for a in str(num)]
        res = sum(nums)
        if res < 10:
            return res
        else:
            return self.addDigits(res)