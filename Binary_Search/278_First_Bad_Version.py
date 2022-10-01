# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        Simple problem, MAKE SURE TO ALWAYS FIX WHILE STATEMENT.
        Draw it out, even if you don't want to, it makes it so much easier.
        TC: O(log(n))
        SC: O(1)
        '''
        low = 1
        high = n
        while low < high:
            print(isBadVersion(high))
            mid = (high + low) // 2
            #if this is true, then we decrease high to mid 
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low