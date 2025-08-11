"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        table = dict()
        tmp = head
        prev = None
        while tmp:
            new_node = Node(tmp.val)
            if prev:
                prev.next = new_node
            table[tmp]=new_node
            prev = new_node
            tmp = tmp.next

        pointer1 = head
        pointer2 = table[head]
        while pointer1 and pointer2:
            random = pointer1.random
            if random:
                pointer2.random = table[random]
            else:
                pointer2.random = None
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return table[head]