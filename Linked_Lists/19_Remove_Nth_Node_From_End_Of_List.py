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
        '''
        Create a dummy node, and set two points equal to it.
        The second pointer will move n times, so that when pointer2
        reaches null, we will remove whichever element p1 is pointing to.
        TC: O(N)
        SC: O(N)
        '''
        dummy = ListNode()
        dummy.next = head
        pointer1, pointer2 = dummy, dummy
        # move pointer2 n times
        for i in range(n):
            pointer2 = pointer2.next
            
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        pointer1.next = pointer1.next.next
        return dummy.next