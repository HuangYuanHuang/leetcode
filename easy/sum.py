
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        self.len = len(nums)
        self.res = []
        for i in range(self.len):
            value = target-nums[i]
            if value in map:
                return [map.get(value),i]
            map[nums[i]]=i
        print(list(map))
        raise RuntimeError('No Find')


sumClass = Solution()
print(sumClass.twoSum([5, 2, 3, 1, 4, 8], 8))
