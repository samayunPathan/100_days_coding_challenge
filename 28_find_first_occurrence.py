def find_index(haystack, needle):
    l1 = len(haystack)
    l2 = len(needle)
    for i in range(l1):
        if haystack[i] == needle[0] and haystack[i:i+l2] == needle:
            return i
    return -1


haystack = 'leetcode'
needle = 'co'

print(find_index(haystack, needle))
