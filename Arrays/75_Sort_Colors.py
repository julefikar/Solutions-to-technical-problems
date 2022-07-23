class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        Make three pointers. One left and one right, and one that is in current index. 
        TC: O(N) One iteration through nums
        SC: O(1) No extra DS is being used
        '''
        left = current = 0
        right = len(nums)-1
        while current <= right: #Equal to because the element where is equal to can be any of the cases.
            if nums[current] == 0: #If it's 0 then we swap current and left. We increment left and current to go to next index.
                nums[left],nums[current] = nums[current],nums[left]
                left += 1
                current += 1
            elif nums[current] == 2: #If current index is a 2, swap it with last index and decrement it.
                nums[current],nums[right] = nums[right],nums[current]
                right -= 1
            else: #It is a 1, increment current
                current += 1