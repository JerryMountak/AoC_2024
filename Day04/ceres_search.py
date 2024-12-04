import numpy as np
import re

def find_xmas(text):
    # Find all occurrences of "XMAS" in the text
    pattern = re.compile(r"XMAS")
    matches = pattern.findall(text)

    return len(matches)

# Part 1
# Read the input file and convert it to a 2D array
with open('input.txt') as file:
    text = [line.strip() for line in file.readlines()]
    text_arr = np.zeros((len(text), len(text[0])), dtype=object)

    for i in range(len(text)):
        for j in range(len(text[0])):
            text_arr[i][j] = text[i][j]

# Convert the text array to a list of strings splitting in lines, columns and diagonals
lines = [''.join(line) for line in text_arr]
lines_reversed = [line[::-1] for line in lines]

columns = [''.join(text_arr[:,j]) for j in range(len(text_arr))]
columns_reversed = [col[::-1] for col in columns]

diags = [''.join(text_arr.diagonal(i)) for i in range(-(len(text_arr)-1),len(text_arr))]
diags_reversed = [diag[::-1] for diag in diags]

orthogonal_diags = [''.join(text_arr[::-1].diagonal(i)) for i in range(-(len(text_arr)-1),len(text_arr))]
orthogonal_diags_reversed = [diag[::-1] for diag in orthogonal_diags]

res = 0
for line in lines:
    res += find_xmas(line)
for line in lines_reversed:
    res += find_xmas(line)
for col in columns:
    res += find_xmas(col)
for col in columns_reversed:
    res += find_xmas(col)
for diag in diags:
    res += find_xmas(diag)
for diag in diags_reversed:
    res += find_xmas(diag)
for ortho_diag in orthogonal_diags:
    res += find_xmas(ortho_diag)
for ortho_diag in orthogonal_diags_reversed:
    res += find_xmas(ortho_diag)

print(f'Part 1: {res}')


# Part 2
def find_x_mas_sliding(text):
    acceptable = {'MAS', 'SAM'}
    # Check if the diagonals of the window have the correct characters
    if ''.join(text.diagonal(0)) in acceptable and ''.join(text[::-1].diagonal(0)) in acceptable:
        return 1
    return 0
    
res = 0
# Iterate the text array using a sliding window of size 3*3
for i in range(len(text_arr)-2):
    for j in range(len(text_arr[0])-2):
        window = text_arr[np.ix_([i, i+1, i+2], [j, j+1, j+2])]

        res += find_x_mas_sliding(window)

print(f'Part 2: {res}')