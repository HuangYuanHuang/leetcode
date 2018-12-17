# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.numA = []
        self.numB = []
        self.treePrint(p, self.numA)
        self.treePrint(q, self.numB)
        if len(self.numA) != len(self.numB):
            return False
        for c in range(len(self.numA)):
            if self.numA[c] != self.numB[c]:
                return False
        return True

    def treePrint(self, root, arr):
        if root:
            arr.append(root.val)
            self.treePrint(root.left, arr)
            self.treePrint(root.right, arr)
        else:
            arr.append(None)
