from functools import cache
import time

def split(rock):
    left, right = rock[:len(rock)//2], rock[len(rock)//2:]
    right = right.lstrip('0')
    if right == '':
        right = '0'
    return left, right

@cache
def blink_recursive(rock, iteration, max_iter):
    if iteration == max_iter:
        return 1
    
    if rock == '0':
        return blink_recursive('1',iteration+1,max_iter)
    elif len(rock)%2 == 0:
        left, right = split(rock)
        return blink_recursive(left,iteration+1,max_iter) + blink_recursive(right,iteration+1,max_iter)
    else:
        return blink_recursive(str(int(rock)*2024),iteration+1,max_iter)


# Part 1
with open('input.txt') as f:
    rocks = f.readline().split()

time_start = time.time()
ans = sum(blink_recursive(rock,0,25) for rock in rocks)

time_end = time.time()
print(f'Part 1: {ans},\t\t\t{time_end - time_start:.4f}s')


# Part 2
time_start = time.time()
ans = sum(blink_recursive(rock,0,75) for rock in rocks)

time_end = time.time()
print(f'Part 2: {ans},\t{time_end - time_start:.4f}s')