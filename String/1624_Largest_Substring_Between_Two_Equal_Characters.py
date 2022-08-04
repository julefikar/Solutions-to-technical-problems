class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        '''
        Make a hashmap of chars and their starting indices.
        If the char repeats then find the distance between the index and original index - 1.
        Return -1 if chars don't repeat
        TC: O(N) where N in length of string
        SC: O(1) String contains only 26 lowercase chars 
        '''
        chars = {}
        largestSS = -1
        for i,val in enumerate(s):
            if val in chars:
                largestSS = max(largestSS, i - chars[val] - 1)
            chars.setdefault(val,i) #Sets the value to first index 
        return largestSS