class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums == None or len(nums) == 0:
            return -1
        if nums[0] > target or nums[-1] < target:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int((left + right) / 2)
            if nums[middle] == target:
                return middle
            else:
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1




if __name__ == '__main__':
    s = Solution()
    s.search([2,5],5)