class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, val in enumerate(nums):
            key = target - val
            if key in dic:
                return [dic[key],i]
            dic[val] = i
        return []