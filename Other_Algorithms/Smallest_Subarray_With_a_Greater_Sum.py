def smallest_subarray_sum(s, arr):
  '''
  Given an array of positive integers and a number ‘S,’ find the length of the 
  smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
  create minSub = 0
  windowSum, windowStart = 0,0
  loop through it, windowEnd.
  windowSum += arr[windowEnd]
  WHILE the subarray is >= s, do minSub=min(minSub, end-start+1)
  subtract arr[windowstart]
  increment windowstart
  return minSub
  TC: O(N+N) You are going through the array, worst case TWO times
  SC: O(1) No extra space is being used 
  '''
  # TODO: Write your code here
  minSub = float("inf")
  windowSum, windowStart = 0,0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]
    while windowSum >= s:
      minSub = min(minSub, windowEnd-windowStart+1)
      windowSum -= arr[windowStart]
      windowStart += 1   
  return minSub
