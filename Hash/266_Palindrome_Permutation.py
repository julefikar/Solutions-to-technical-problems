class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        Simple problem, a palindrome can have max one char that is odd
        If more than one char, then it is false
        TC: O(N) where n is len(s)
        SC: O(1) 26 lowercase letters, so constant
        '''
        chars = Counter(s)
        exceptions = 0 
        for char in s:
            if chars[char] % 2 == 1:
                exceptions += 1
            if exceptions > 1:
                return False
        return True