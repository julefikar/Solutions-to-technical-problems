class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Do two pointer. Be careful of indexes. 
        Make a window: If next element of left is greater, increment it. 
        Stop when next index is smaller.
        If previous element of right is smaller, decrement it. 
        Stop when previous is larger.
        Find the max and min of subarray.
        WHILE the element before the subarray is bigger than minimum, decrement left.
        WHILE the element after the subarray is smaller than maximum, increment right.
        TC: O(N) Multiple while loops but shortens to O(N) where N is number of elements in arr.
        SC: O(1) No extra DS used.
        '''
        length = len(nums)
        l = 0
        r = length - 1
        while l < length - 1 and nums[l] <= nums[l+1]:
            l += 1
        if l == length - 1: #Array is already sorted
            return 0
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        #Find subarray max and min
        subArrayMin = float("inf")
        subArrayMax = float("-inf")
        for i in range(l,r+1):
            subArrayMin = min(subArrayMin, nums[i])
            subArrayMax = max(subArrayMax, nums[i])
        
        while l > 0 and nums[l-1] > subArrayMin:
            l -= 1
        while r < length - 1 and nums[r+1] < subArrayMax:
            r += 1
        
        return r-l+1