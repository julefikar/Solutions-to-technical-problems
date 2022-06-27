class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        Do binary search, which halves the amount of values it is searching for. If number is greater than target, decrease the right.
        If target is smaller, increase the left. Else, just returns the middle number.
        TC: O(log(n))
        SC: O(1)
        '''
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2 #REASON IT IS O(LOG(N))
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1