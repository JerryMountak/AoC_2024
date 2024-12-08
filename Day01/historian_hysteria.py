import time

# Part 1
left = []
right = []

# Read the input
with open('input.txt') as input:
    lines = input.readlines()

    for line in lines:
        a, b = line.split()
        a = int(a)
        b = int(b)
        left.append(a)
        right.append(b)

time_start = time.time()
# Sort the lists
left.sort()
right.sort()

res = 0
for i,j in zip(left, right):
    res += abs(i - j)

time_end = time.time()
print(f'Part 1: {res},\t{time_end - time_start:.3f}s')


# Part 2
# Calculate the number frequency in the right list
time_start = time.time()
freq = {}
for i in right:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

res = 0

for i in left:
    if i in freq:
        res += i*freq[i]

time_end = time.time()
print(f'Part 2: {res},\t{time_end - time_start:.3f}s')