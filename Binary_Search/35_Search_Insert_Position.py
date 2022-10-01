class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Simple, needed to put edgecase where the target can be greater than last index.
        TC:O(log(n))
        SC:O(1)
        '''
        low = 0
        high = len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        while low < high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return high