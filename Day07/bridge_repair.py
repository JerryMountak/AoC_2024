from itertools import product
import time

def eval_expression(values, operators):
    ops = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
        '||': lambda a, b: int(f'{a}{b}')
    }
    
    res = values[0]    
    for value, operator in zip(values[1:], operators):
        res = ops[operator](res, value)

    return res

def is_eq_true(equation, operators):
    res, values = equation

    num_operators = len(values)-1
    operators_list = list(product(operators, repeat=num_operators))
    
    for ops in operators_list:
        if eval_expression(values, ops) == res:
            return True
        
    return False


# Part 1
equations = []

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        res, values = line.split(':')
        values = values.strip().split(' ')

        equations.append((int(res), tuple(map(int, values))))

time_start = time.time()
ans = 0
for equation in equations:
    res, values = equation

    if is_eq_true(equation, ['+','*']):
        ans += res

time_end = time.time()
print(f'Part 1: {ans},\t{time_end - time_start:.3f}s')


# Part 2
time_start = time.time()
ans = 0
for equation in equations:
    res, values = equation
    
    if is_eq_true(equation, ['+','*','||']):
        ans += res

time_end = time.time()
print(f'Part 2: {ans},\t{time_end - time_start:.3f}s')
