class Solution:
    '''
    Check which side from mid is sorted and go off that. 
    TC: O(log(n))
    SC: O(1)
    '''
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if target != nums[0] else 0
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: #left to mid is sorted properly do binary search here
                if target >=nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
                
            else: #mid+1 to right is sorted
                if target <=nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 
                
                