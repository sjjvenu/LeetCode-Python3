class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numdic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        count = len(digits)
        if count == 0:
            return []
        if count == 1:
            if digits[0] in numdic:
                return list(numdic[digits[0]])
            else:
                return []
        if count == 2:
            l1 = list(numdic[digits[0]])
            l2 = list(numdic[digits[1]])
            s = list()
            for m in l1:
                for n in l2:
                    s.append(m+n)
            return s
        else:
            left = 0
            right = count
            middle = count/2
            list1 = self.letterCombinations(digits[int(left):int(middle)])
            list2 = self.letterCombinations(digits[int(middle):int(right)])
            s = list()
            for m in list1:
                for n in list2:
                    s.append(m+n)
            return s


class Solution1:
    def letterCombinations(self, digits):
        """
        :type
        digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        numdic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        combs = ['']
        for s1 in digits:
            combsTemp = []
            for comb in combs:
                for s2 in numdic[s1]:
                    combsTemp.append(comb+s2)
            combs = combsTemp


        return combs




if __name__ == '__main__':
    s = Solution1()
    print(s.letterCombinations('234'))
