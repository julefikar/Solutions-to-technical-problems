class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        If first occurance, we move right down and update ans
        If last occurance, we move left up and update ans
        TC: O(logn)
        SC: O(1)
        '''
        left = 0
        right = x
        ans = 0
        while left <=right:
            mid = left + (right - left) // 2
            if mid*mid > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
                
        return ans