class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Two pointer problem.
        TC: O(N), it is O(4N) -> O(N).
        SC: O(1) No extra space is being used.
        '''
        if len(nums) <= 1: #We cannot see if it is in order since it's only one value
            return 0 
        l = 0
        r = len(nums) - 1
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]: #WHILE the next index is higher than this index, increase it. 
            l+=1
        while r > 0 and nums[r] >= nums[r - 1]: #WHILE the next index is smaller than this index, decrease it. 
            r-=1
        if l>r: #If for any reason the left is greater than the right, it must mean the array is sorted properly.
            return 0
        #Find the local max and min
        localMax = max(nums[l:r+1])
        localMin = min(nums[l:r+1])
        while l>0 and localMin < nums[l-1]: #WHILE the previous element is bigger than localMin, decrement it.
            l-=1
        while r<len(nums)-1 and localMax > nums[r+1]: #While the next element is smaller than the localMax, increment it.
            r+= 1
        return r-l+1 #Returns the window length
        