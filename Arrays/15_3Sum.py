class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        Two pointer problem
        TC: O(N^2) two loops used, must iterate through array n^2 times.
        SC: O(N) Extra space used
        '''
        ans = []
        nums.sort() #Sorting the array will make the indices easier to operate two pointer solution.
        for i in range(len(nums)-2): #-2 because there consists of three elements here, the index, left, and right pointer.
            l = i+1
            r = len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum == 0:
                    ans.append([nums[i],nums[l],nums[r]]) #If we find that it equals to 0, append it and move l and r pointers, so case is not repeated.
                    l += 1
                    r -= 1
                elif currentSum < 0: #Increment if smaller
                    l += 1
                else: r -= 1 #Decrement if bigger
        actualAns = []
        for key in ans: #Removing duplicates
            if key not in actualAns:
                actualAns.append(key)
        return actualAns