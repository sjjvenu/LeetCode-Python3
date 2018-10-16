# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        head.next = ListNode(0)
        l3 = head.next
        sign = 0
        while l1 != None or l2 != None:
            if l1 != None:
                l3.val += l1.val
                l1 = l1.next
            if l2 != None:
                l3.val += l2.val
                l2 = l2.next
            l3.val += sign
            if l3.val >= 10:
                l3.val -= 10
                sign = 1
            else:
                sign = 0
            if l1 != None or l2 != None:
                l3.next = ListNode(0)
                l3 = l3.next

        if sign == 1:
            l3.next = ListNode(1)
            l3 = l3.next
            
        return head.next


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(4)
    l1.next.next = ListNode(8)
    l1.next.next.next = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    s.addTwoNumbers(l1,l2)
