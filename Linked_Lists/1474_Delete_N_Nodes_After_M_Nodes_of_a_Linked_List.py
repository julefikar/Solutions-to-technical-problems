# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Kind of hard to grasp but it makes sense. Needed help.
    Have a previous pointer which follows the head and is only used when iterating through M.
    When it is done skipping n times, make the previous's next pointer to the head and repeat
    until end of LL.
    TC: O(N) 1 pass
    SC: O(1)
    '''
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None,head)
        prev = head
        
        while head:
            numM = m
            numN = n
            
            while head and numM > 0:
                prev = head
                head = head.next
                numM -= 1
            while head and numN > 0:
                head = head.next
                numN -= 1
            
            prev.next = head
        
        return dummy.next