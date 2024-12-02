def check_report(report):
    diffs = [abs(a - b) for a,b in zip(report, report[1:])]

    # Check if the report is sorted or reverse sorted
    if (report == sorted(report)) or (report == sorted(report, reverse=True)):
        # Check if the diffs are all between 0 and 4
        safe = all(map(lambda x: 0 < x < 4, diffs))
    else:
        safe = False

    return safe, diffs


# Part 1
reports = []

# Read the input
with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        reports.append(list(map(int, line.split())))

safe_reports = 0

# Check each report
for report in reports:
    safe,_ = check_report(report)
    
    if safe:
        safe_reports += 1

print(f'Part 1: {safe_reports}')


# Part 2
safe_reports = 0

for report in reports:
    safe, diffs = check_report(report)

    sort_mask = [0 if x > y else 1 for x,y in zip(report, report[1:])]
    diff_mask = [0 if 0 < x < 4 else 1 for x in diffs]
    
    if safe:
        safe_reports += 1
    else:
        majority = max(set(sort_mask), key = sort_mask.count)
        flag = False
        g = (i for i, e in enumerate(diff_mask) if e == 1)
        for i in g:
            rep = report.copy()
            rep.pop(i+1)
            s,_ = check_report(rep)
            if s:
                safe_reports += 1
                flag = True
                break

            rep = report.copy()
            rep.pop(i)
            s,_ = check_report(rep)
            if s:
                safe_reports += 1
                flag = True
                break
        if not flag:
            g = (i for i, e in enumerate(sort_mask) if e != majority)
            for i in g:
                rep = report.copy()
                rep.pop(i+1)
                s,_ = check_report(rep)
                if s:
                    safe_reports += 1
                    flag = True
                    break

                rep = report.copy()
                rep.pop(i)
                s,_ = check_report(rep)
                if s:
                    safe_reports += 1
                    flag = True
                    break

print(f'Part 2: {safe_reports}')