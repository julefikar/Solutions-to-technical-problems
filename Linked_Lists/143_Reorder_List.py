# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        Make a fast and slow pointer. When fast reaches end, slow will be at middle.
        Reverse the second part from slow. 
        Starting from head, make every other node point to the reverse list.
        TC: O(N) N is number of nodes
        SC: O(1) No extra DS used
        '''
        fast, slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #Now slow is at middle, reverse it from here.
        prev, current = None, slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        #Now previous is reversed 2nd half of list
        #Combine them together, let first equal the head
        first, second = head, prev
        while second.next:
            first.next, first = second,first.next
            second.next, second = first, second.next
            
    
            