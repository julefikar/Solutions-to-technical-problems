class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        Two pointer solution.
        TC: O(N^2) Iterating through the array n^2 times.
        SC: O(1) No extra DS is being used
        '''
        n = len(nums)
        if n < 3:
            return 0
        nums.sort() #Sorting will make it easier to use two pointer
        count = 0 #Counting the number of triplets
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l<r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum < target:
                    count += r-l #If it is smaller, then all the indices between right and left pointer are also smaller.
                    l += 1 #Increase the left pointer to get more valid cases
                else: 
                    r -= 1 #If above is not satisfied, then the right value is too high, so we decrease it
        return count
                    
                
                
            
        