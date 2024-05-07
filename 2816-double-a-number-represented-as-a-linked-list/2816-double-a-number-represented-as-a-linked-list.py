# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def traverseAndDouble(head):
            if not(head):
                return 0
            carry = traverseAndDouble(head.next)
            result=head.val*2+carry
            head.val=(head.val*2+carry)%10
            return result //10
        last_carry=traverseAndDouble(head)
        if last_carry:
            new_head= ListNode(last_carry,head)
            # while new_head:
            #     print(new_head.val, end=' ')
            #     new_head = new_head.next
            return new_head
        return head
             
            