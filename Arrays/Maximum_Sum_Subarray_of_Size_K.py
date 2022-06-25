'''
Problem Statement#
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

Do a sliding window approach. Counts the first k indices, makes maxSum equal to whatever it is. 
Then increment the window by one, and keep doing it until the array is complete.
TC: O(N)
SC: O(1)
'''
def max_sub_array_of_size_k(k, arr):
  maxSum, windowStart, windowSum = 0,0,0
  for windowIndex in range(len(arr)):
    windowSum += arr[windowIndex]
    maxSum = max(maxSum, windowSum)
    if windowIndex >= k-1:
      windowSum -= arr[windowStart]
      windowStart += 1
  return maxSum
