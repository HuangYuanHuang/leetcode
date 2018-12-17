# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = current = ListNode(0)
        while l1 or l2:
            newNode = ListNode(0)
            current.next = newNode
            current = newNode
            if not l1:
                newNode.val = l2.val
                l2 = l2.next
            elif not l2:
                newNode.val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                newNode.val = l1.val
                l1 = l1.next
            else:
                newNode.val = l2.val
                l2 = l2.next
        return root.next
