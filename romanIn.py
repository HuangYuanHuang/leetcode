# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
