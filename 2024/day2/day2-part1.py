file = open('day2.txt', 'r')
content = file.read()
lists = content.splitlines()

safe = []
unsafe = []

for list in lists:
    split_lists = list.split(' ')

    is_safe = True
    direction = None
    
    for i in range(1, len(split_lists)):
        difference = int(split_lists[i]) - int(split_lists[i -1])
        difference_abs = abs(int(split_lists[i]) - int(split_lists[i -1]))

        if difference_abs < 1 or difference_abs > 3:
            is_safe = False
            break

        if direction is None:
            direction = 'increasing' if difference > 0 else 'decreasing'

        elif (direction == 'increasing' and difference < 0) or (direction == 'decreasing' and difference > 0):
            is_safe = False
            break

    if is_safe:
        safe.append(split_lists)
    else:
        unsafe.append(split_lists)

print(len(safe))
