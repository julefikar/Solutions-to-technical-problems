class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num = {}
        maxInt = -1
        for digits in nums:
            num[digits] = num.get(digits, 0) + 1
        
        for keys in num.keys():
            if num[keys] == 1:
                maxInt = max(maxInt,keys)
        return maxInt
            
        
        
                