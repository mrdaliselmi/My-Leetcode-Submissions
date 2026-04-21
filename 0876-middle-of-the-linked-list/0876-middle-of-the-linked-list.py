# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length = 0
        temp = head
        while temp:
            temp=temp.next
            length+=1
        temp = head
        for i in range(length//2):
            temp=temp.next
        return temp