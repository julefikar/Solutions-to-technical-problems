class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        Make a function where it appends the remainder of x in an array. Then reverse the array to see if it is a palindrome.
        *121 % 10 = 1
        121 // 10 = 12
        *12 % 10 = 2
        12 // 10 = 1
        *1 % 10 = 1
        1 // 10 = 0
        new array will be: 1,2,1
        return array == array[::-1] (reversed)
        '''
        if x < 0: #Negative numbers will never be palindromes.
            return False
        digits = []
        digit = None
        while x!=0:
            digit = x % 10
            digits.append(digit)
            x //= 10
        return digits==digits[::-1]
        
        