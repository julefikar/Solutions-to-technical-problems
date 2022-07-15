'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''
'''
Two pointer solution
TC: O(N^2)
SC: O(N) creating a new array
'''
def search_triplets(arr):
  arr.sort() #Sorting the array will make it so we can use two pointer.
  triplets = [] 
  n = len(arr) 
  for i in range(n-2): #N-2 because the last two elements can prove to be sum to 0.
    left = i + 1 #Next element after i
    right = n - 1 #Last element
    while (left < right):
      valNeeded = -arr[i] # Value needed to make it equal 0
      if arr[left] + arr[right] < valNeeded: #If sum is less than value needed, we need to increase left because it is sorted.
        left += 1
      elif arr[left] + arr[right] > valNeeded: #If sum is greater than value needed, we need to decrease right because it is sorted.
        right -= 1
      else: #If equal, we append values. And move pointers up.
        triplets.append([-valNeeded,arr[left],arr[right]])
        left += 1
        right -=1 
  return triplets

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  #print(search_triplets([-5, 2, -1, -2, 3]))


main()
