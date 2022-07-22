class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        Sliding window problem. Divide last element while the product is greater/equal to k. And increment window.
        *SLIDING WINDOW ONLY WORKS BECAUSE NUMBERS ARE POSITIVE AND NUMBERS ARE INTEGERS  
        TC: O(N), O(2N) because while loop is running its course while it is true in our for loop
        SC: O(1) No extra DS used
        '''
        if k <= 1: #Product has to be bigger
            return 0
        counter, left = 0,0
        product = 1 #Have to make it 1 because 1*x = x
        for right,val in enumerate(nums): #Enumerate because we want index and value. Will display "0,value at index 0"
            product *= val #Multiplies to the 
            while product >= k: #While statement because it can occur multiple times
                product /= nums[left] #Get rid of previous element and increment window
                left += 1
            counter += right - left + 1 #Adds the spaces to counter
        return counter
                
            
            