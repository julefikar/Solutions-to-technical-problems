class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Actually a pretty hard problem, I misunderstood it many times. I thought there was going to be duplicates.
        I eventually looked up solution, do a binary search on both sides of array. 
        TC: O(log(n))
        SC: O(1)
        '''
        def binarySearchLeft(nums,target,left,right):
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        
        def binarySearchRight(nums,target,left,right):
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        
        if len(nums) == 0:
            return [-1,-1]
        
        left = 0
        right = len(nums) - 1
        left = binarySearchLeft(nums,target,left,right)
        right = binarySearchRight(nums,target,left,right)
        return [left,right]
            