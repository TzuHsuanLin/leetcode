class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = [1]
        n1 = n2 = n3 = 0
        tmp = 0
        for i in range(n):
            tmp = min(num[n1] * 2, num[n2] * 3, num[n3] * 5)
            num.append(tmp)
            if tmp == num[n1] * 2:
                n1 += 1
            if tmp == num[n2] * 3:
                n2 += 1
            if tmp == num[n3] * 5:
                n3 += 1
        print(num)
        return num[n-1]