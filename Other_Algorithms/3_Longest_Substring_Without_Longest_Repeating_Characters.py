class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Make a hashset to store the characters, do a sliding window approach.
        chars = set()
        longestSubstring = 0
        windowStart = 0
        for windowEnd in range(len(s)):
            if windowEnd is in set:
                remove WINDOWSTART from set
                increment starting window
            add windowEnd to hashset
            longestSub = max(longestSub, end-start+1)
        return longestSubstring
        TC: O(N) Looping through len of string, at most N+N times
        SC: O(N) Extra memory used; hashset.
        '''
        
        chars = set()
        longestSubstring = 0
        windowStart = 0
        for windowEnd in range(len(s)):
            while s[windowEnd] in chars:
                chars.remove(s[windowStart])
                windowStart += 1
            chars.add(s[windowEnd])
            longestSubstring = max(longestSubstring,windowEnd-windowStart+1)
        return longestSubstring
        
        
        