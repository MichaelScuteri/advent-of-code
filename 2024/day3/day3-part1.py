import re

with open('day3.txt', 'r') as file: 
    content = file.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, content)

    totals = []

    for item in matches:
        total = int(item[0]) * int(item[1])
        totals.append(total)

    print(sum(totals))