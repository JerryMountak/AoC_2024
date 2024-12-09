from copy import deepcopy
import time

# Function to create the expanded representation of the disk map
def expand(disk_map):
    expanded = []
    id = 0
    for i,block in enumerate(disk_map):
        if i%2 == 0:
            for _ in range(block):
                expanded.append(str(id))
            id += 1
        else:
            for _ in range(block):
                expanded.append('.')

    return expanded

# Function to defrag the expanded disk map moving individual blocks
def rearrange_blocks(expanded_map):
    blocks = deepcopy(expanded_map)
    filled_blocks = sum(True for block in expanded_map if block != '.')

    while True:
        i = next(i for i,v in enumerate(blocks) if v == '.')
        if i < filled_blocks:
            j = next(len(blocks)-i-1 for i,v in enumerate(blocks[::-1]) if v != '.')

            blocks[i], blocks[j] = blocks[j], blocks[i]
        else:
            break
    
    return blocks

# Function to get the filled and empty block details of the disk map
def get_disk_status(disk_map):
    tmp = deepcopy(disk_map)
    filled = []
    empty = []
    last_ind = 0
    for i,block in enumerate(tmp):
        if i%2 == 0:
            filled.append((last_ind,block,i//2))
        else:
            empty.append((last_ind,block))
        last_ind += block
    
    return filled,empty

# Function to defrag the disk map moving individual files
def rearrange_files(disk_map):
    files = deepcopy(disk_map)
    filled, empty = get_disk_status(files)

    for i,(ind,value,temp) in enumerate(filled[::-1]):
        for j,(id_e,count) in enumerate(empty):
            if ind < id_e:
                break
            elif value > count:
                continue
            else:
                empty.pop(j)
                if value != count:
                    empty.insert(j, (id_e+value, count-value))
                filled[len(filled)-i-1] = (id_e,value,temp)
                break

    return filled

# Function to calculate the checksum of the disk map
def checksum(blocks):
    return sum(int(block)*i for i,block in enumerate(blocks) if block != '.')

# Function to calculate the sum of consecutive numbers
def sum_consecutive(num, times):
    times = times - 1
    return ((2*num + times) * (times + 1)) // 2


# Part 1
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        disk_map = list(map(int, line.strip()))

time_start = time.time()
ans = checksum(rearrange_blocks(expand(disk_map)))
time_end = time.time()
print(f'Part 1: {ans},\t{time_end - time_start:.4f}s')


# Part 2
time_start = time.time()
b = sorted(rearrange_files(disk_map), key=lambda x: x[0])
ans = 0
for file in b:
    ans += sum_consecutive(file[0],file[1])*file[2]

time_end = time.time()

print(f'Part 2: {ans},\t{time_end - time_start:.4f}s')