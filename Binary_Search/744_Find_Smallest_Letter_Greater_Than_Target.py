class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        Needed help with this problem, had the basic jist of it. Also didn't read it carefully - about the looping bounds. 
        Didn't know what to return at the end, do more test cases before writing the solution!!!
        TC: O(log(n))
        SC: O(1)
        '''
        #Handles the looping bounds
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        low = 0
        high = len(letters) - 1
        while low<=high:
            mid = low + (high - low) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return letters[low]
        