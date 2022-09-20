class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Took a bit of time to think out. We use left < right when we are setting a certain value to JUST mid. 
        TC: O(log(n))
        SC: O(1)
        '''
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            #Valid case can be written because bounds can't be peak.
            validCase = (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1])
            if validCase:
                   return mid
            if nums[mid] > nums[mid+1]:
                   right = mid 
            else:
                   left = mid + 1
        return left