# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.arr = [0]*n
        self.arr[0] = self.arr[1] = 1
        self.arr[2] = 2
        return self.getN(n)

    def getN(self, n):
        if self.arr[n] != 0:
            return self.arr[n]
        self.arr[n] = self.getN(n-1)+self.getN(n-2)
        return self.arr[n]
