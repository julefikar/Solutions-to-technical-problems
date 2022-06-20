# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        Make current going to head pointer. And previous equal to NULL. We want the next pointer to trace back to the previous pointer, 
        and make the previous pointer go to the current node, then make the current the next node until it's NULL. We return the previous,
        because the head will start at end of list.
        TC: O(N)
        SC: O(1)
        '''
        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous