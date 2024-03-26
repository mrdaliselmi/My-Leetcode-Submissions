# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = list()
        while head:
            l.append(head.val)
            head = head.next
        return l[:int(len(l)/2)] == l[:-int(len(l)/2)-1:-1]