from copy import deepcopy
import sys
sys.path.append('..')
from utils import Direction

class LoopException(Exception):
    pass

# Function to simulate the movement of the guard
def traverse(lab_map, pos, visited_pos, detect_circle=False):
    direction = Direction.Up

    while True:
        # Check for loop
        if detect_circle:
            if (*pos, direction) in visited_pos:
                raise LoopException
            visited_pos.add((*pos, direction))   
        else:
            visited_pos.add(pos)

        new_pos = direction.move(pos)

        # Check if the new position is in bounds
        if new_pos[0] < 0 or new_pos[0] >= len(lab_map) or new_pos[1] < 0 or new_pos[1] >= len(lab_map[0]):
            return
        
        # Check if new position is an obstacle
        if lab_map[new_pos[0]][new_pos[1]] == '#':
            direction = direction.turn_clockwise()
            continue

        pos = new_pos


# Part 1
# Read the input file
with open('input.txt') as f:
    lines = f.readlines()
    lab_map = []

    for i, line in enumerate(lines):
        line = list(line.strip())
        if '^' in line:
            guard_pos = (i, line.index('^'))
        
        lab_map.append(line)
        
visited = set()
traverse(lab_map, guard_pos, visited)
print(f'Part 1: {len(visited)}')


# Part 2
res = 0
visited.remove(guard_pos)
for x,y in visited:
    lab_copy = deepcopy(lab_map)
    lab_copy[x][y] = '#'
    vis_copy = set()
    try:
        traverse(lab_copy, guard_pos, vis_copy, detect_circle=True)
    except LoopException:
        res += 1

print(f'Part 2: {res}')