class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        '''
        Was thinking too hard, used a hashmap that worked for half the examples.
        This one just looks at the next two chars and if they are all distinct, then increment count. 
        TC: O(N) N is len(s)
        SC: O(1) Constant space used
        '''
        count = 0
        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                count += 1
        return count