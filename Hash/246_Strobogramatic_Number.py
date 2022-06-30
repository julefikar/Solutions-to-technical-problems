class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        '''
        0 -> 0
        1 -> 1
        6 -> 9
        8 -> 8
        9 -> 6
        Create a hashmap containing those digits and their mappings. Create two pointers, if left num doesn't match right num OR
        it is not in mappings, return false. Return true if all these cases pass.
        TC: O(N)
        SC: O(1) constant extra space used
        '''
        mappings={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        left = 0
        right = len(num) - 1
        while left<=right:
            if num[left] not in mappings or (mappings[num[left]]!=num[right]): #It is supposed to match every case if Strobogramatic
                return False
            left += 1
            right -= 1
        return True
            