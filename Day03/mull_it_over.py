import re

# Match muls and do/don't using regex
def match_muls(input, extended=False):
    reg = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")
    res = []
    for match in reg.finditer(input):
        try:
            res.append((int(match.group(1)), int(match.group(2))))
        except TypeError:
            if extended:
                res.append(True if match.group(0) == "do()" else False)
            else:
                continue

    return res


# Part 1
# Read the input file
with open('input.txt') as f:
    input = f.read()

# Match only muls for part 1
nums = match_muls(input)

ans = 0
for pair in nums:
    ans += pair[0] * pair[1]

print(f'Part 1: {ans}')


# Part 2
# Match muls and do/don't operations
dirs = match_muls(input, extended=True)

ans = 0
enabled = True
for dir in dirs:
    if type(dir) is bool:
        enabled = dir
        continue
    
    if enabled:
        if type(dir) is not bool:
            ans += dir[0] * dir[1]

print(f'Part 2: {ans}')