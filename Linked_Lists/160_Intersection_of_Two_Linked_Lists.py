# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''
        1. Make edge cases, if either is empty.
        2. Create a hashset where you iterate through headA and add it's pointer values.
        3. In a second iteration, if headB is in the hashset, return that pointer value.
        4. Return None if no intersection.
        TC: O(N+M) = O(N) iterating through two lists N+M
        SC: O(N) Additional memory (set) is used.
        '''
        if not headA or not headB:
            return None
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        while headB:
            if headB in visited:
                return headB
            headB=headB.next
        return None
        