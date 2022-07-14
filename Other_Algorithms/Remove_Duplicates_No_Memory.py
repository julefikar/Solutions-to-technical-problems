'''
Given an array of sorted numbers, remove all duplicate number instances from it in-place, 
such that each element appears only once. The relative order of the elements should be kept the same and 
you should not use any extra space so that that the solution have a space complexity of O(1).
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Make two pointers, one that should that the next element is a non duplicate.
When the last non duplicate element doesn't equal the current element, 
    we have to make sure that the index of the non duplicated element equals current index.
    Increment the non_duplicate counter
increment the index counter
TC: O(N)
SC: O(1)
'''
def remove_duplicates(arr):
    if not arr: #Empty input
        return None 
    next_non_duplicate = 1
    i = 0
    while i < len(arr):
        if arr[next_non_duplicate-1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
