# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        current = root = ListNode(0)
        preValue = head.val-1
        while head:
            if head.val != preValue:
                newNode = ListNode(head.val)
                preValue = head.val
                current.next = newNode
                current = newNode
            head = head.next
        return root.next
