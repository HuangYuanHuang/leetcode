# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        listStack = []
        dictMap = {'(': 1, '{': 2, '[': 3, ')': -1, '}': -2, ']': -3}
        for c in s:
            temp = dictMap[c]
            if temp > 0:
                listStack.append(temp)
            elif listStack and listStack.pop() == abs(temp):
                pass
            else:
                return False
        return len(listStack) == 0

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == '(':
                stack.append(')')
            elif not stack or c != stack.pop():
                return False
        return not stack


print(
    Solution().isValid("()([]){}")
)
