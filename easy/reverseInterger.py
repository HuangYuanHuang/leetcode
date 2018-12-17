class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        pre = 1 if x > 0 else -1
        x = abs(x)
        min = -(1 << 31)
        max = (1 << 31) - 1
        print(min, max, 2**31)
        while x > 0:
            res = res*10+x % 10
            x = x // 10
        if res >= 2**32:
            return 0
        return res*pre


print(Solution().reverse(1563847412))
print(123 % 10, 123//10)
