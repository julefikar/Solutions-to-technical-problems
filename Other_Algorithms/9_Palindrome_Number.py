class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        IGNORE THIS SOLUTION! 
        Make a function where it appends the remainder of x in an array. Then reverse the array to see if it is a palindrome.
        *121 % 10 = 1
        121 // 10 = 12
        *12 % 10 = 2
        12 // 10 = 1
        *1 % 10 = 1
        1 // 10 = 0
        new array will be: 1,2,1
        return array == array[::-1] (reversed)
        
        if x < 0: #Negative numbers will never be palindromes.
            return False
        digits = []
        digit = None
        while x:
            digit = x % 10
            digits.append(digit)
            x //= 10
        return digits==digits[::-1]
        '''
        '''
        Follow previous technique but instead of array just make it a variable and see if values are equal to each other.
        TC: O(log(n))
        SC: O(1)
        '''
        if x < 0: #Negative numbers will never be palindromes.
            return False
        revNum = 0
        num = x
        while num:
            revNum = revNum * 10 + num%10
            num/=10
        return x == revNum
            
            