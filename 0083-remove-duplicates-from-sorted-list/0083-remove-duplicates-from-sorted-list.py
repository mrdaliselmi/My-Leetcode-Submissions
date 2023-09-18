# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(next=head)
        ptr1,ptr2=dummy,head
        s=set()
        while ptr2:
            if ptr2.val in s:
                ptr1.next = ptr2.next
                ptr2=ptr1.next
            else:
                s.add(ptr2.val)
                ptr1=ptr1.next
                ptr2=ptr1.next
        return dummy.next