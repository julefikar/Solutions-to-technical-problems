class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        We look at the occurances of each char.
        If frequency is even: always add it because any amount of even numbers can make palindrome,
        If odd: Add frequency and subtract one because there can only be one odd number we add.
        Make the number of oddChar = 1
        TC: O(N) where N is len(s)
        SC: O(1) Constant extra space used, input only upper/lower chars
        '''
        chars = Counter(s)
        length = 0
        oddChar = 0
        for i in chars.values():
            if i % 2 == 0: #It is even
                length += i
            else: #If it is odd
                length += i - 1
                oddChar = 1
        return length + oddChar
                
                
                