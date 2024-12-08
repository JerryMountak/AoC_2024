import time
import numpy as np

# Function to find the Manhattan distance between two points
def manhattanDistance(x,y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

# Function to generate all Manhattan points with a given distance from a point
def generateManhattanPoints(x, y, r):
    points = set()
    for offset in range(r):
        invOffset = r - offset # Inverse offset
        points.add((x + offset, y + invOffset))
        points.add((x + invOffset, y - offset))
        points.add((x - offset, y - invOffset))
        points.add((x - invOffset, y + offset))
    return points

def filterPoints(points, grid_size):
    return set(point for point in points if 0 <= point[0] < grid_size[0] and 0 <= point[1] < grid_size[1])

# Function to calculate the angle between two points
def angleBetween(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return np.arctan2(dy, dx)


# Part 1

# Read the input file and create a 2D array for the antenna map
# Store the antenna types and their corresponding points in a dictionary
antenna_types = {}
with open('input.txt') as f:
    lines = f.readlines()
    antenna_map = np.zeros((len(lines),len(lines[0])-1), dtype=object)

    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            antenna_map[i,j] = char
            if char == '.':
                continue
            if char not in antenna_types:
                antenna_types[char] = [(i,j)]
            else:
                antenna_types[char].append((i,j))

time_start = time.time()
nodeMap = set()
for antenna, points in antenna_types.items():
    for point in points:
        for otherPoint in points:
            if point == otherPoint:
                continue

            # Calculate the Manhattan distance between the two points and 
            # generate all possible antinodes
            dist = manhattanDistance(point, otherPoint)
            pointNodes = generateManhattanPoints(*point, dist)
            otherNodes = generateManhattanPoints(*otherPoint, dist*2)

            # Keep only the common points and filter out points that are not within the grid
            antiNodes = pointNodes.intersection(otherNodes)
            antiNodes = filterPoints(antiNodes, (len(lines),len(lines[0])-1))
            
            # Keep only the antinodes in line with the antennae
            angles = {angleBetween(point, otherPoint), angleBetween(otherPoint, point)}
            antiNodes = set(node for node in antiNodes if angleBetween(point, node) in angles)
            nodeMap.update(antiNodes)

time_end = time.time()
print(f'Part 1: {len(nodeMap)},\t{time_end - time_start:.3f}s')


# Part 2
time_start = time.time()
nodeMap = set()
for antenna, points in antenna_types.items():
    for point in points:
        for otherPoint in points:
            if point == otherPoint:
                continue
            
            # Calculate the valid angles for the antinodes
            angles = {angleBetween(point, otherPoint), angleBetween(otherPoint, point)}
            
            # iterate the grid and keep only the nodes that are in the valid angles
            for i in range(len(antenna_map)):
                for j in range(len(antenna_map[0])):
                    node = (i,j)
                    if angleBetween(point, node) in angles:
                        nodeMap.add(node)

time_end = time.time()
print(f'Part 2: {len(nodeMap)},\t{time_end - time_start:.3f}s')
