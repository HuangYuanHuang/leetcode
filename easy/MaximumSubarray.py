# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = nums[0]
        for num in nums:
            sum += num
            if sum > res:
                res = sum
            if sum < 0:
                sum = 0
        return res


Solution().maxSubArray([-2, -1])
