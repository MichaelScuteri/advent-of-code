file = open('day1/day1.txt', 'r')
content = file.read()
lists = content.splitlines()

list1 = []
list2 = []

for line in lists:
    left, right = line.split()
    list1.append(int(left))
    list2.append(int(right))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

variances = []

for item1, item2 in zip(sorted_list1, sorted_list2):
    difference = abs(item1 - item2) 
    variances.append(difference)

print(sum(variances))