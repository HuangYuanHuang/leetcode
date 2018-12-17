# https://leetcode.com/problems/add-two-numbers/
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
        arrA = []
        arrB = []
        resArr = []
        while currentNodeA is not None:
            arrA.append(currentNodeA.val)
            currentNodeA = currentNodeA.next
        while currentNodeB is not None:
            arrB.append(currentNodeB.val)
            currentNodeB = currentNodeB.next
        lenA = len(arrA)
        lenB = len(arrB)
        maxLen = (lenA if lenA > lenB else lenB)
        carry = 0
        for index in range(maxLen):
            value = carry
            if index < lenA:
                value += arrA[index]
            if index < lenB:
                value += arrB[index]
            resArr.append(value % 10)
            carry = value//10
            if carry > 0 and index+1 >= maxLen:
                resArr.append(carry)

        resRoot = root = ListNode(0)
        print(resArr)
        for index in range(len(resArr)):
            root.next = ListNode(resArr[index])
            root = root.next
        return resRoot.next


nodeA = ListNode(1)
# nodeA.next = ListNode(4)

nodeB = ListNode(9)
nodeB.next = ListNode(9)

Solution().addTwoNumbers(nodeA, nodeB)
