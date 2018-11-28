class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                print(count(a))
                ans.append(a)
        return ans
            
    def wordSubsets2(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        ccb={}
        for b in B:
            cb={}
            for l in b:
                if l in cb:
                    cb[l]+=1
                else:
                    cb[l]=1
            for l in b:
                if l not in ccb or ccb[l]<cb[l]:
                    ccb[l]=cb[l]
                    
        Bcounter = ccb
        ret = []
        for a_s in A:
            for k in Bcounter:
                if a_s.count(k) < Bcounter[k]: break
                else:
                    ret.append(a_s)
        return ret



if __name__ == '__main__':
    s = Solution()
    print(s.wordSubsets2(["amazon","apple","facebook","google","leetcode"],["e","oo"]))
