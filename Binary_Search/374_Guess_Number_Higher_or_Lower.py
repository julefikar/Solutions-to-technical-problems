# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    '''
    Simple problem, rushed to do it and flipped the low/high conditions. Besides that, was straight forward.
    TC: O(log(n))
    SC: O(1)
    '''
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while (low<=high):
            mid = low + (high - low) // 2
            pick = guess(mid)
            if pick == 0:
                return mid
            elif pick == -1:
                #low = mid + 1
                high = mid - 1
            else:
                #high = mid - 1
                low = mid + 1
        return -1