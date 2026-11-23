# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        even = ListNode()
        even_tmp = even
        tmp = head
        while tmp:
            if tmp.next:
                # add to even
                even_tmp.next = tmp.next
                even_tmp = even_tmp.next
                # remove even from list
                tmp.next = tmp.next.next
                # clean even next
                even_tmp.next = None
            tmp = tmp.next
        tmp = head
        while tmp.next:
            tmp = tmp.next
        tmp.next = even.next
        return head