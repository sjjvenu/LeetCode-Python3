class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        list = set()
        for email in emails:
            name,_,domain = email.partition('@')
            if '+' in name:
                name = name[:name.index('+')]
            list.add(name.replace('.','')+'@'+domain)
        return len(list)
            


if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
