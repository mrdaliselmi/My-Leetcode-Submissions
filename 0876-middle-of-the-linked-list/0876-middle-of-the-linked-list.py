# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        length = 0
        while dummy.next:
            length +=1
            dummy = dummy.next
        middle = round(length / 2)
        for _ in range(int(middle)):
            head = head.next
        return head