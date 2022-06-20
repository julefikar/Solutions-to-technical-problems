class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """''' O(nlogn) sorted solution
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: 
                count+=1
        return (count>=1)
        '''
        '''
        We can use a HashTable to store values, if value of any key is 2 or more, return true. Else false. 
        TC: O(N)
        SC: O(N)
        '''
        vals = {}
        for num in nums:
            if num not in vals:
                vals[num] = 1
            else:
                return True
        return False
                