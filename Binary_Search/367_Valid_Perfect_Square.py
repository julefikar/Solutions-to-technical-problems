class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        Done within 2-3 minutes. The only condition to return true is if there is a number between 1-num,
        which squared == num. 
        TC: O(log(n))
        SC: O(1)
        '''
        low = 1
        high = num
        while low <= high:
            mid = (high+low) // 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared < num: #Increase low to meet mid+1
                low = mid + 1
            else: #Decrease high to meet m-1 because that squared can be ans.
                high = mid - 1
        return False #False if no numbers in between 1-num.