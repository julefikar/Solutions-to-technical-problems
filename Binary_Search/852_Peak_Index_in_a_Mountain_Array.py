class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        '''
        Needed help on this problem. 
        Didn't realize that peak can't be first or last index. Could have checked bounds. 
        Ex: arr[peak-1] < peak < arr[peak+1]
        The conditions to move pointers were also easy to see but didn't come to my brain :(
        TC: O(log(n))
        SC: O(1)
        '''
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (right + left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left