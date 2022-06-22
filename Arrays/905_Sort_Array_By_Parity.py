class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start=0
        for end in range(len(nums)):
            if nums[end]%2 ==0: #If it is even, change the values.
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
        return nums