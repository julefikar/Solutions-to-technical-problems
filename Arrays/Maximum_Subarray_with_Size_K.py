'''
Given an array of positive numbers and a positive k, find maximum sum of subarray of size k.
ex:
[2,1,5,1,3,2] K= 3
output: 9 because subarray with max sum is [5,1,3]

[2,3,4,1,5] k = 6
-1 because k is larger than the array.
'''
'''
This is a sliding window because we have to find a specific subarray within a contigious array.
TC: O(N)
SC: O(1)
'''
def getMaxSum(arr, k):
    # Write your code here
    if k > len(arr):
        return -1
    maxSum, windowStart, windowSum = float("-inf"),0,0 #Create three variables, set values appropiate to it.
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] #Add the windowEnd to the sum of window
        if windowEnd - windowStart >= k - 1: #When the window is size of K. K-1 because indices start at 0.
            maxSum = max(maxSum, windowSum) #We are keeping track of max, so max it everytime the window size is K.
            windowSum -= arr[windowStart] #Subtract the original windowStart from the sum for the new sum 
            windowStart += 1 #Increment windowStart
    return maxSum
