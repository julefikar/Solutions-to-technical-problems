# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    '''
    Easy binary search marked as medium, all you have to do is basic BS with diff function.
    TC: O(log(N)) where N is unknown length of array
    SC: O(1)
    '''
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        high = 10**4
        while low <= high:
            mid = (high + low) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1