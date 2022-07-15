'''
Given an input string, write a function that returns the run-length encoded string for the input string

Example:
Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"
'''
'''
Use two pointers, and compare next char to current char. While next char is same, keep adding the count
Concatenate the count after while loop ends. Then increment index by that count.
TC: O(N)
SC: O(1)
'''
def rle(s):
    l = len(s)

    result = ''
    if l == 0:
        return result

    i = 0
    while i < l:
        char = s[i]
        result += char
        count = 1
        while i + count < l and s[i + count] == char:
            count += 1
        result += str(count)
        i += count
        
    return result

def main():
    print(rle("aaaabbbbbbaaaa"))

main()
        