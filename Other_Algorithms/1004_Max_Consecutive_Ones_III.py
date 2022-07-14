class Solution(object):

    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        Create a hashmap that records the values of 0 and 1, initialize them to 0. Do a sliding window.
        WHILE the frequency of 0 is greater than k, subtract arr[windowStart] from HM and then increment wS.
        Use the max function to record longest substring length. Return that.
        TC: O(N) O(N+N) 
        SC: O(1) Uses only two extra memory.
        '''
        hm = {0:0,1:0}
        (windowStart, longest) = (0, 0)
        for windowEnd in range(len(nums)):
            right = nums[windowEnd]
            hm[right] = hm.get(right, 0) + 1
            while hm[0] > k:
                hm[nums[windowStart]] -= 1
                windowStart += 1
            longest = max(longest, windowEnd - windowStart + 1)
        return longest
