# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        1. Create a new array (arr) and append value of each node, creating a copy of the linked list.
        2. Reverse it (arr[::-1]), if equal to arr, then return true, if not then return false.
        TC: O(N)
        SC: O(N) because of adding N elements to new array
        '''
        arr = []
        current = head
        while current is not None:
            arr.append(current.val)
            current = current.next
        return arr == arr[::-1]
            
            