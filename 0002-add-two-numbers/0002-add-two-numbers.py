# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ""
        while l1:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        s2 = ""
        while l2:
            s2 = s2 + str(l2.val)
            l2 = l2.next
        s1 = s1[::-1]
        s2 = s2[::-1]
        r = int(s1) + int(s2)
        r = str(r)[::-1]
        result = ListNode()
        l = result
        for i in range(len(str(r))-1):
            l.val = int(str(r)[i])
            l.next = ListNode()
            l = l.next
        l.val = int(str(r)[-1])
        return result