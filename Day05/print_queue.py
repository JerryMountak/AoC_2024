import time

# Function to check if a list conforms to a rule
def check_ordering(rule, nums):
    seen_rule_first = False
    for num in nums:
        if num == rule[1] and not seen_rule_first:
            return False
        elif num == rule[0]:
            return True
    return True

# Part 1
rules = []
updates = []

# Read in the input file and split it into rules and updates
with open('input.txt') as file:
    lines = file.readlines()

    for line in lines:
        if "|" in line:
            rule = line.split("|")
            rules.append((int(rule[0]), int(rule[1])))
        elif line == '\n':
            continue
        else:
            updates.append(list(map(int, line.split(','))))

time_start = time.time()
valid_updates = []
has_rules = []

for update in updates:
    pages = set(update)

    all_valid = True
    rule_list = []
    for rule in rules:
        # If update doesn't contain both pages, skip
        if rule[0] in pages and rule[1] in pages:
            is_valid = check_ordering(rule, update)
            rule_list.append(True)
            if not is_valid:
                all_valid = False
        else:
            rule_list.append(False)
    
    # Save rules used in this update
    has_rules.append(rule_list)
    
    if all_valid:
        valid_updates.append(True)
    else:
        valid_updates.append(False)

ans = 0
for i,update in enumerate(updates):
    if valid_updates[i]:
        ans += update[len(update)//2]

time_end = time.time()
print(f"Part 1: {ans},\t{time_end - time_start:.3f}s")


# Part 2
# Funtion to fix ordering of list according to rule
def fix_ordering(rule, nums):
    ind_ins = nums.index(rule[1])
    ind_pop = nums.index(rule[0])

    # Slide the first element of the rule to the left until it's before the secondelement
    nums.pop(ind_pop)
    nums.insert(ind_ins, rule[0])

time_start = time.time()
res = []
for i,update in enumerate(updates):
    if not valid_updates[i]:
        ordered_rules = sorted([rules[j] for j,rule in enumerate(has_rules[i]) if rule], key=lambda x: x[0])
        ordered_list = []
        for rule in ordered_rules:
            if rule[1] not in ordered_list:
                # If the list is empty, just add the first two elements
                if rule[0] not in ordered_list:
                    ordered_list.append(rule[0])
                    ordered_list.append(rule[1])
                else:
                    # If the second element isn't on the list but the first is, add the second to the end
                    ordered_list.append(rule[1])
            # If the first element isn't on the list, add just before the second element
            elif rule[0] not in ordered_list:
                ind = ordered_list.index(rule[1])
                ordered_list.insert(ind, rule[0])
            else:
                # If both elements are on the list, check if they're in the right order
                if not check_ordering(rule, ordered_list):
                    fix_ordering(rule, ordered_list)
        
        res.append(ordered_list)

ans = 0
for update in res:
    ans += update[len(update)//2]

time_end = time.time()
print(f"Part 2: {ans},\t{time_end - time_start:.3f}s")
