class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        Two pointer solution. 
        Make a new array that stores all the squared values. Initialize all of it to 0.
        Have a third pointer which just points to the last value. We want the last value to be greatest.
        Do regular two pointer algo where whichever pointer is bigger, initialize squares[highestSquare] to it.
        Whichever condition it meets, increment or decrement that pointer, if left, increase it. If right, decrease it.
        Decrement the highestSquare pointer. And return result.
        TC: O(N) - O(2N), two iterations are run -> O(N)
        SC: O(N) extra space used for the output array
        '''
        squares = [0 for i in range(len(nums))]
        x = len(nums)
        l = 0
        r = x - 1
        highestSquare = x - 1
        while l <= r:
            leftSquare = nums[l] * nums[l]
            rightSquare = nums[r] * nums[r]
            if leftSquare > rightSquare:
                squares[highestSquare] = leftSquare
                l += 1
            else:
                squares[highestSquare] = rightSquare
                r -= 1
            highestSquare -= 1
        return squares
            