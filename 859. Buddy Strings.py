class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        if len(A) != len(B) or len(A) <= 1 or len(B) <= 1:
            return False
        index1 = 0
        index2 = 0
        count = 0
        dic = {}
        for i in range(len(A)):
            if A[i] in dic:
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
            if A[i] != B[i]:
                count += 1
                if count == 1:
                    index1 = i
                else:
                    if count == 2:
                        index2 = i
                    else:
                        if count > 2:
                            return False
        if index1 == index2:
            for key in dic:
                if dic[key] > 1:
                    return True
            return False
        strTemp = A[index1]
        alist = list(A)
        alist[index1] = alist[index2]
        alist[index2] = strTemp
        A = ''.join(alist)
        if A == B:
            return True
        else:
            return False
            


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings('abab','abab'))
