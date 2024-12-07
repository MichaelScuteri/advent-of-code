import re

with open('day3.txt', 'r') as file:
    content = file.read()
    content = re.sub(r"don't\(\).*?(?=do\(\)|$)", "", content, flags=re.DOTALL)

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, content)

    totals = []

    for match in matches:
        total = int(match[0]) * int(match[1])
        totals.append(total)

    print(sum(totals))


