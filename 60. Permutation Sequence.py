class Solution:
    def factorial(self,x):
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result


    def helper2(self,nums,target):
        """
        :type nums: list
        :type k: int
        :rtype: list
        """
        k = target
        if self.factorial(len(nums)) < k:
            return []
        count = len(nums)
        if count == 1 or k == 1:
            return nums
        if self.factorial(count) == k:
            return nums[::-1]
        ret = []
        if self.factorial(count) > k and self.factorial(count-1) < k:
            index = int(k/self.factorial(count-1))
            k = k-index*self.factorial(count-1)
            if k == 0:
                index = index-1
                k = target - index * self.factorial(count - 1)
            ret.append(nums[index])
            nums.remove(nums[index])
            tempNums = self.helper2(nums,k)
            ret.extend(tempNums)
        else:
            for i in range(count-1,-1,-1):
                if self.factorial(count-i) >= k:
                    ret.extend(nums[:i])
                    tempNums = self.helper2(nums[i:],k)
                    ret.extend(tempNums)
                    return ret

        return ret



    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        if self.factorial(n) < k:
            return ''
        originList = [n for n in range(1, n + 1)]

        ret = self.helper2(originList,k)
        return ''.join(str(x) for x in ret)
            


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3,4))
