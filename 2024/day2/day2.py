file = open('day1/day1input.txt', 'r')
content = file.read()
lists = content.splitlines()

list1 = []
list2 = []

for line in lists:
    left, right = line.split()
    list1.append(int(left))
    list2.append(int(right))

for num in list1:
    #need to create a dictionary to store the count and also the number counted 
    total = list2.count(num)
    print(total)



    