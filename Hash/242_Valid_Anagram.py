class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        Create two HashMaps, one for s and one for t. Traverse through it, if all vals of s match all vals of t, return True. Else false.
        TC: O(3N) = O(N)
        SC: O(2N) = O(N)
        '''
        if len(s) != len(t):
            return False
        counter = {}
        for i in s: #Puts values of s into counter
            if i not in counter:
                counter[i] = 1
            counter[i] += 1
        
        counter_t = {}
        for i in t: #Puts values of t into counter
            if i not in counter_t:
                counter_t[i] = 1
            counter_t[i] += 1
            
        for chars in s:
            if ((chars in counter_t) and (chars in counter)): #Checks if they both chars exists in both hashmaps, return false if values don't match.
                if counter[chars] != counter_t[chars]:
                    return False
            else:
                return False
        return True