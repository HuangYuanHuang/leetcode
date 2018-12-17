# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.split()
        [].append
        if temp == []:
            return 0
        else:
            return len(temp[-1])


print(Solution().lengthOfLastWord("a "))