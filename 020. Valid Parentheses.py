class Solution:

    def remove(self, s1, s2):
        if (s1 == '{' and s2 == '}') or (s1 == '[' and s2 == ']') or (s1 == '(' and s2 == ')'):
            return True
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        stack = ''
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack = s[i] + stack
            else:
                if len(stack) > 0 and self.remove(stack[0], s[i]):
                    stack = stack[1:]
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True

        return False



class Solution2:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        
        pDict = { ')':'(', ']': '[', '}':'{' }
        pStack = [s[0]]
        
        for i in s[1:]: 
            if i not in pDict:
                pStack.append(i)
            elif (len(pStack) != 0) and (pDict[i] == pStack[-1]):
                pStack.pop()
            else: 
                pStack.append(i)
                
        if len(pStack) == 0:
            return True
        else:
            return False 
            


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{}[]'))
