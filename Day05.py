int_list = []

with open('Day05.input', 'r') as input_data:
    for line in input_data:
        num = int(line.strip())
        int_list.append(num)

# Part 1
pos = 0
count = 0
finish = len(int_list)
while pos < finish:
    if int_list[pos] == 0:
        int_list[pos] = 2
        pos += 1
        count += 2
    elif pos + int_list[pos] < finish:
        curr_val = int_list[pos]
        next_val = int_list[curr_val + pos]
        jump = curr_val + next_val
        count += 2
        int_list[curr_val + pos] += 1
        int_list[pos] += 1
        if jump == 0:
            int_list[pos] += 1
            pos += int_list[pos] - 1
            count += 1
        else:
            pos += jump
    else:
        int_list[pos] = int_list[pos] + 1
        pos = pos + int_list[pos] - 1
        count += 1

print count #351282

# Part 2
int_list = []

def get_modifier(pos):
    modifier = 1
    if int_list[pos] >= 3:
        modifier = -1
    return modifier

with open('Day05.input', 'r') as input_data:
    for line in input_data:
        num = int(line.strip())
        int_list.append(num)
pos = 0
count = 0
modifier = 1
finish = len(int_list)
while pos < finish:
    if int_list[pos] == 0:
        int_list[pos] = 2
        pos += 1
        count += 2
    elif pos + int_list[pos] < finish:
        curr_val = int_list[pos]
        next_val = int_list[curr_val + pos]
        jump = curr_val + next_val
        count += 2
        int_list[curr_val + pos] += get_modifier(curr_val + pos)
        int_list[pos] += get_modifier(pos)
        if jump == 0:
            modifier = get_modifier(pos)
            int_list[pos] += modifier
            pos += int_list[pos] - modifier
            count += 1
        else:
            pos += jump
    else:
        modifier = get_modifier(pos)
        int_list[pos] = int_list[pos] + modifier
        pos = pos + int_list[pos] - modifier
        count += 1

print count #24568703
