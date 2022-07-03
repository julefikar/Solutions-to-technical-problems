def longest_substring_with_k_distinct(str1, k):
  '''
  araaci k=2
  v
       v
  h = {}
  maxSubstring = float("-inf")
  windowStart = 0
  FOR LOOP:
    add windowend to hashmap
    maxSubstring = max(maxSubstring, end-start)
    while the keys of hashmap > k: 
      hashmap subtract val -1
        if val is 0: delete
      increment windowstart
  "araa" = end-start to find len of substring
  return the maxSubstring
  TC: O(N) Even though it has a while statement in it, doesn't make it N^2. Both pointers have to go through
  the answer ONE time.
  SC: O(N) Used extra DS to keep character count.
  '''
  # TODO: Write your code here
  h = {}
  maxSubstring = float("-inf")
  windowStart = 0
  for windowEnd in range(len(str1)):
    right_letter = str1[windowEnd]
    h[right_letter]=h.get(right_letter,0)+1
    while len(h) > k:
      left_letter = str1[windowStart]
      h[left_letter]-=1
      if h[left_letter]==0:
        del h[left_letter]
      windowStart += 1
    maxSubstring = max(maxSubstring, windowEnd - windowStart + 1)
  return maxSubstring
