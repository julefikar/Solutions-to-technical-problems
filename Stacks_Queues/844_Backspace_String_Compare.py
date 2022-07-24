class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        Stack solution.
        TC: O(N) actually N+M where N and M are lengths of S and T
        SC: O(N) actually N+M where N and M are lengths of S and T
        '''
        def comparer(string):
            arr = []
            for s in string: #If it isn't a #, add it to arr. If anything else, pop it.
                if s != "#":
                    arr.append(s)
                elif arr: #It can't be empty. You can't pop empty array.
                    arr.pop()
            return "".join(arr) #Concatenate the elements of the arr.
        return comparer(s) == comparer(t)