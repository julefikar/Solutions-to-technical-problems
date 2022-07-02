class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Check if it is alphanumeric, and use two pointers to see if left equals right pointer.
        TC: O(N) N depends on length of array, iterating through it N times.
        SC: O(1) No extra memory is used.
        '''
        left  = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            else:
                if s[left].lower() != s[right].lower():
                    return False
            left+=1
            right-=1
        return True