# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        Disappointed at myself for taking so long to do this, even needed help. Had the right idea,
        couldn't execute it.
        TC: O(N)
        SC: O(1)
        '''
        dummyNode = ListNode()
        dummyNode.next = head
        current = head
        previous = dummyNode
        print(current)
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return dummyNode.next