import time
import sys
sys.path.append("..")
from utils import get_neighbors

# Function to recursively hike the trail from a starting point
def hike_trail(grid, x, y, visited=None):
    if isinstance(visited, set):
        if (x,y) in visited:
            return 0
        visited.add((x,y))
    
    if grid[x][y] == 9:
        return 1
    
    head_value = grid[x][y]
    neighbors = get_neighbors(grid, x, y, value=head_value+1)

    ans = 0
    for neighbor in neighbors:
        ans += hike_trail(grid, neighbor[0], neighbor[1], visited)
    return ans


# Part 1
grid = []
trail_heads = []

# Read the input file
with open("input.txt") as file:
    lines = file.readlines()

    # Keep track of the trail heads
    for i,line in enumerate(lines):
        nums = list(map(int, list(line.strip())))
        for k in (j for j,n in enumerate(nums) if n == 0):
            trail_heads.append((i,k))
        grid.append(nums)

time_start = time.time()
ans = 0
for head in trail_heads:
    visited = set()
    ans += hike_trail(grid, *head, visited)

time_end = time.time()
print(f"Part 1: {ans},\t{time_end - time_start:.4f}s")


# Part 2
time_start = time.time()
ans = 0
for head in trail_heads:
    ans += hike_trail(grid, *head)

time_end = time.time()
print(f"Part 2: {ans},\t{time_end - time_start:.4f}s")
