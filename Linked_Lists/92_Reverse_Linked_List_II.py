# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummyNode = ListNode()
        dummyNode.next = head
        leftPrev, current = dummyNode,head
        
        #Make our previous pointer at the node before current(left position)
        for i in range(left-1):
            leftPrev,current = leftPrev.next,current.next
            #print(leftPrev.val,current.val)
        
        #Reverse it right-left+1 times
        previous = None
        for i in range(right-left+1):
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        
        leftPrev.next.next = current
        leftPrev.next = previous
        
        return dummyNode.next