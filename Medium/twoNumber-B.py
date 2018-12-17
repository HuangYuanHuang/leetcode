# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        currentNodeA = l1
        currentNodeB = l2
        resRoot = root = ListNode(0)
        carry = 0
        while True:
            value = carry
            if currentNodeA is not None:
                value += currentNodeA.val
                currentNodeA = currentNodeA.next
            if currentNodeB is not None:
                value += currentNodeB.val
                currentNodeB = currentNodeB.next
            newNode = ListNode(value % 10)
            root.next = newNode
            root = root.next
            carry = value//10
            if currentNodeA is None and currentNodeB is None:
                if carry > 0:
                    newNode.next = ListNode(carry)
                break
        return resRoot.next
