# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        res = ListNode(0, head)
        tmp = res
        while tmp.next and tmp.next.next:
            first = tmp.next
            second = first.next

            first.next = second.next
            second.next = first

            tmp.next = second

            tmp = first

        return res.next