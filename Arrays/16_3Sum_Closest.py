class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        Two pointer problem
        TC: O(N^2) two loops used, must iterate through array n^2 times.
        SC: O(1) no extra space used
        '''
        nums.sort() #Sorting the array will make the indices easier to operate two pointer solution.
        res = sum(nums[:3]) #Sum of the first three numbers. This CAN change.
        for i in range(len(nums)-2): #-2 because there consists of three elements here, the index, left, and right pointer.
            l = i+1
            r = len(nums) - 1
            while l<r:
                currentSum = nums[i] + nums[l] + nums[r] #Sum of the current iteration
                if abs(currentSum-target) < abs(res-target): #Whichever has the lowest difference, make that the new result.
                    res = currentSum
                if currentSum < target: #If number is smaller than target, increment left
                    l += 1
                elif currentSum > target: #If number is bigger than target, decrement right
                    r -= 1
                else: return res #It is equal so return the result
        return res
                    
                
        
        