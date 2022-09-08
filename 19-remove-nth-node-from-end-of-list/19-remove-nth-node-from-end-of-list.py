# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None and n == 1:
            return None
        
        def reverse(node, prev):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        dummy = reverse(head, None)
        
        if n == 1:
            dummy = dummy.next
            return reverse(dummy, None)
       
        count = 1
        prev = None
        node = dummy
        while count != n:
            count += 1
            prev = dummy
            dummy = dummy.next
        
        prev.next = dummy.next
        
        return reverse(node, None)
            