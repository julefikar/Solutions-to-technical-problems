class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        Solved it originally passing 250/280ish testcases but couldn't solve it fully,
        needed help. 
        Similar to the previous search in rotated sorted array problem with few caveats.
        There can be repeated elements, so the conditions do have to change.
        With this exception, the worst case is actually O(N).
        This is where most elements in the array are != target and are equal to each other.
        TC: O(log(n)) - best, O(N) worst
        SC: O(1)
        '''
        
        if len(nums) == 1:
            return target == nums[0]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            #shifting to all the duplicate elements, worst case O(N)
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1
            
            mid = (right + left) // 2

            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False