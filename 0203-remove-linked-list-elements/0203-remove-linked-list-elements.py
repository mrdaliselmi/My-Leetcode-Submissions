# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy=ListNode(next= head)
        ptr1,ptr2=dummy,head
        
        while ptr2:
            if ptr2.val == val:
                ptr1.next = ptr2.next
                ptr2=ptr1.next
            else:
                ptr1=ptr1.next
                ptr2=ptr1.next
        return dummy.next