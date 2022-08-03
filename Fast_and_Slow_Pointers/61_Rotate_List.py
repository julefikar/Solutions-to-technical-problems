# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Use fast and slow pointer.
    Find length of Linked List
    Move fast pointer by k%length times
    When we reach end of LL. Whatever slow.next is gets cut off
    Make a cycle by making fast.next = head
    Make head start at the slow.next 
    Cut off slow.next 
    Mistakes: Not knowing how to do it :(! 
    Improvements: Think about using fast/slow pointers when having to do anything cycle related.
    TC: O(N) N is number of nodes
    SC: O(1) No extra DS being used
    '''
    def findLength(self, head):
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #head = [1,2,3,4,5], k = 2
        if k == 0:
            return head
        if not head:
            return None
        
        fast,slow = head,head
        offset = k % self.findLength(head) #Modulo by length of LL because k can be larger than length
        for i in range(offset):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head #Making it a cycle
        # 1 2 3 4 5 1 2 3 4 5...
        head = slow.next #Making head start at slow.next (4) in this case
        # 4 5 1 2 3 4 5 1 2 3... 
        slow.next = None #Cutting off the cycle, by making the next None
        
        return head