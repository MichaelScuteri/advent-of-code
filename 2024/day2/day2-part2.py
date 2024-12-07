with open('day2.txt', 'r') as file: content = file.read()
lists = content.splitlines()

safe = []
unsafe = []

def check_safe(split_lists):
    direction = None

    for i in range(1, len(split_lists)):
        difference = int(split_lists[i]) - int(split_lists[i -1])
        difference_abs = abs(int(split_lists[i]) - int(split_lists[i -1]))

        if difference_abs < 1 or difference_abs > 3:
            return False

        if direction is None:
            direction = 'increasing' if difference > 0 else 'decreasing'

        elif (direction == 'increasing' and difference < 0) or (direction == 'decreasing' and difference > 0):
            return False
    
    return True

for list in lists:
    split_lists = list.split(' ')
    is_safe = check_safe(split_lists)

    if is_safe:
        safe.append(split_lists)
    else:
        can_be_safe = False

        for num in range(len(split_lists)):
            temp_list = split_lists[:num] + split_lists[num + 1:]
            if check_safe(temp_list):
                can_be_safe = True
                break
        
        if can_be_safe:
            safe.append(split_lists)
        else:
            unsafe.append(split_lists)

print(len(safe))
