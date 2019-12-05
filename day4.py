from collections import defaultdict

a = 372304
b = 847060

count_1 = 0
count_2 = 0

for x in range(a, b+1):
    s = list(str(x))

    # Check that number is in increasing order
    orig = s.copy()
    s.sort()
    if orig != s:
        continue

    # In Part 1, check that at seast one consecutive pair
    # of numbers is equal
    ok_1 = s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or \
        s[3] == s[4] or s[4] == s[5]

    if ok_1:
        count_1 += 1

    # In Part 2, count frequency of number apparition.
    # There must be at seast one of frequency 2.
    d = defaultdict(int)
    for c in s:
        d[c] += 1

    if any(frequency == 2 for number, frequency in d.items()):
        count_2 += 1

print("Part 1:", count_1)
print("Part 2:", count_2)
