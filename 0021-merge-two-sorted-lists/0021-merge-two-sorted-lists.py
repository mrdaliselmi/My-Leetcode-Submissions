# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res=ListNode()
        ptr=res
        while list1 and list2:               
            if list1.val <= list2.val:
                ptr.next = list1
                list1, ptr = list1.next, list1
            else:
                ptr.next = list2
                list2, ptr = list2.next, list2
                
        if list1 or list2:
            ptr.next = list1 if list1 else list2
            
        return res.next
