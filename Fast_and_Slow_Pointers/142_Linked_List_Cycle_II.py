# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
First see if it a cycle because if not return -1
If cycle, we find length of cycle
Using length of cycle, increment the fast pointer from beginning by length of cycle
And then increment slow and fast by one node, UNTIL THEY MEET. 
Also add a counter from start starting at 0 to see the index at which they meet.
Mistakes: Read problem carefully. Know how to declare global variables. 
TC: O(N) 
SC: O(1) No additional DS being used
'''
class Solution:
    def lengthOfCycle(self, slow):
        counter = 0
        current = slow
        while current:
            current = current.next
            counter += 1
            if current == slow:
                break
        return counter

    def findIndice(self, head, lengthCycle):
        fast,slow = head,head
        for i in range(lengthCycle):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast, slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                lengthCycle = self.lengthOfCycle(slow)
                return self.findIndice(head, lengthCycle)
        return None