class Solution:
    
    def helper(self,s,left,right,k):
        if right - left < k:
            return 0
        dic = {}
        for c in s[left:right]:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for i in range(left,right):
            if dic[s[i]] < k:
                j = i+1
                while j < right and dic[s[j]] < k:
                    j += 1
                return max(self.helper(s,left,i,k),self.helper(s,j,right,k))
            
        return right-left
    
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.helper(s,0,len(s),k)
            


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("ababacb",3))
