# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # ptr=head
        # hashset=set()
        # if ptr==None:
        #     return False
        # while ptr.next !=None:
        #     if ptr.next in hashset:
        #         return True
        #     else:
        #         hashset.add(ptr.next)
        #         ptr=ptr.next
        # return False
        slow, fast=head, head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False