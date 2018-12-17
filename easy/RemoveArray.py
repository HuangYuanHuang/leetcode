# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrSet = set(nums)
        index = 0      
        resArr=list(arrSet)
        resArr.sort()
        for i in resArr:
            nums[index] = i
            index+=1
        return len(arrSet)


nums = [-1,0,0,0,0,3,3]
arrLen = Solution().removeDuplicates(nums)
for c in range(arrLen):
    print(c, nums[c])
