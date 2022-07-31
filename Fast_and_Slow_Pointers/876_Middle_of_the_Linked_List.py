# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Use a fast and slow pointer, when fast is null or fast.next is null.
Return the slow pointer.
TC: O(N) where N is number of nodes
SC: O(1) no extra DS is being used
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow