class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        countLeft = 0
        countRight = 0
        for s in S:
            if s == '(':
                countLeft +=1
            else:
                if countLeft > 0:
                    countLeft -= 1
                else:
                    countRight += 1
        
        return countLeft+countRight
            


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid('(((((('))
