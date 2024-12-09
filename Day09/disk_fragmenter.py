from copy import deepcopy
import time

# Function to get the filled and empty block details of the disk map
def get_disk_status(disk_map, expand=False):
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

    if expand:
        filled_expanded = []
        for index,reps,value in filled:
            filled_expanded.extend([(index+i,value) for i in range(reps)])
        
        filled = filled_expanded    
    return filled,empty

# Function to defrag the disk map moving individual blocks
def rearrange_blocks(disk_map):
    blocks = deepcopy(disk_map)
    filled, empty = get_disk_status(blocks, expand=True)
    
    for i,(index_b,value) in enumerate(filled[::-1]):
        for j,(index_e,count) in enumerate(empty):
            if index_b < index_e:
                break
            else:
                if count == 0:
                    continue
                empty[j] = (index_e+1, count-1)
                filled[len(filled)-i-1] = (index_e,value)
                break

    return filled

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
block_defrag = rearrange_blocks(disk_map)
ans = 0
for file in block_defrag:
    ans += sum_consecutive(file[0],1)*file[1]
time_end = time.time()
print(f'Part 1: {ans},\t{time_end - time_start:.4f}s')


# Part 2
time_start = time.time()
file_defrag = rearrange_files(disk_map)
ans = 0
for file in file_defrag:
    ans += sum_consecutive(file[0],file[1])*file[2]

time_end = time.time()

print(f'Part 2: {ans},\t{time_end - time_start:.4f}s')