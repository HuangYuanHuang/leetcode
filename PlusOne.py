# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        re = []
        pre = 0
        digits[-1] += 1
        print(digits)
        for c in reversed(digits):
            if c+pre >= 10:
                pre = 1
                re.insert(0, 0)
            else:
                re.insert(0, c+pre)
                pre = 0
        if pre>0:
            re.insert(0,1)
        return re


print(Solution().plusOne([1, 9]))
