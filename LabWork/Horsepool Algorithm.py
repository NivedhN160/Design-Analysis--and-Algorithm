# Write a Python program to implement Horspool’s Algorithm for string matching.

def build_shift_table(pattern):
    m = len(pattern)
    shift_table = {}

    for i in range(m - 1):
        shift_table[pattern[i]] = m - 1 - i

    return shift_table


def horspool_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m > n:
        return -1

    shift_table = build_shift_table(pattern)
    i = m - 1

    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1

        if k == m:
            return i - m + 1

        shift = shift_table.get(text[i], m)
        i += shift

    return -1


# Input
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

# Searching
position = horspool_search(text, pattern)

# Output
if position != -1:
    print("Pattern found at index:", position)
else:
    print("Pattern not found")