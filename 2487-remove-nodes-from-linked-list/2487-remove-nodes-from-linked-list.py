# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def findNewHead(head):
            if head.next is None:
                return head
            new_head = findNewHead(head.next)
            if head.val >= new_head.val:
                head.next = new_head
                return head
            return new_head
        return findNewHead(head)