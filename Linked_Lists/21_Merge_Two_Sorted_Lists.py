# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        '''
        Create a dummyNode to get rid of null head. 
        Traverse through both lists, whichever value is smaller, add it to tails next.
        If done traversing, add the rest of nodes to whichever one is not empty.
        TC: O(N+M)
        SC: O(N+M)
        '''
        dummyNode = ListNode() #incase Empty head is provided
        tail = dummyNode
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1: #If it is not empty add it to end of list
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummyNode.next #We return at next node because we don't want NULL as first value.
            