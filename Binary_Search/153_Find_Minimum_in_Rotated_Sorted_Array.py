class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Solved in 23 min, happy I got it done. 
        Very similar to the find element in rotated array.
        If mid is less than left element, we have to decrease right to mid-1
        Same can be said when nums[left] < nums[right], we know number has to be before mid
        TC: O(log(n))
        SC: O(1)
        '''
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        lowest = float("inf")
        while left <= right:
            mid = (right + left) // 2
            lowest = min(lowest,nums[mid])
            if nums[mid] < nums[left] or nums[left] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return lowest