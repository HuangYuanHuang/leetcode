# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        res=(nums1[:m]+nums2[:n])
        res.sort()
        index=0
        for c in res:
            nums1[index]=c
            index+=1
