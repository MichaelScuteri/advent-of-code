file = open('day1/day1.txt', 'r')
content = file.read()
lists = content.splitlines()

list1 = []
list2 = []

for line in lists:
    left, right = line.split()
    list1.append(int(left))
    list2.append(int(right))

duplicates = []

for num in list1:
    total = list2.count(num)
    if total != 0:
        total *= num
        duplicates.append(total)

print(sum(duplicates))



    