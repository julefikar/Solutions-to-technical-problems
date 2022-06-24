class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        Create a hashmap, if complement is in it. Return index of iteration and the index of complement.
        TC: O(N)
        SC: O(N)
        '''
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dictionary:
                return [i, dictionary[complement]]
            dictionary[nums[i]] = i
        return -1
        
        