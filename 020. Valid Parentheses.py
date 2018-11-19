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


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{}[]'))
