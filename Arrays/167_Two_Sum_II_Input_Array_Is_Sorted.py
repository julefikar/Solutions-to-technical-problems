class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        Since it is already sorted for us, we can use two pointers. Compare the first element with the last element, if the pointer sum
        is target, we are guaranteed exactly ONE solution, so just return that +1 because the indices start from 0. If current sum is smaller,
        increment the left to make sum greater. If sum is larger than target, decrement right. 
        TC: O(N) One loop is needed, we iterate through array once.
        SC: O(1) No extra space is used.
        '''
        length = len(numbers)
        l = 0
        r = length - 1
        while l<r:
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return [l+1,r+1]
            elif currentSum < target:
                l += 1
            else:
                r -= 1