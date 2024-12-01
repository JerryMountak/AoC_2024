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

# Sort the lists
left.sort()
right.sort()

res = 0
for i,j in zip(left, right):
    res += abs(i - j)

print(f'Part 1: {res}')


# Part 2
# Calculate the number frequency in the right list
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

print(f'Part 2: {res}')