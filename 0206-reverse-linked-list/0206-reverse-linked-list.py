# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f,s=head,head.next if head else None
        if f:
            f.next=None
        while f and s:
            n=s.next
            s.next=f
            f=s
            s=n
        return f