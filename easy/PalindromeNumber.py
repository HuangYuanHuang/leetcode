# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.code = str(x)
        self.len = len(self.code)
        for index in range(self.len//2):
            print(self.code[index], self.code[self.len-index-1])
            if self.code[index] != self.code[self.len-index-1]:
                return False
        return True

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.code = str(x)
        if self.code[::-1] == self.code:
            return True
        return False


print(Solution(). isPalindrome(101))
