import math

#Part 1 definition
coords = {1:(0,0)}
max_coords = {'left':(0,0),
           'right':(0,0),
           'up':(0,0),
           'down':(0,0)}

start = 1
end = 368080
current = start

current_coords = coords[current]
while current <= end:
    #go left
    while current_coords[0] <= max_coords['right'][0]:
        current += 1
        current_coords = (current_coords[0] + 1,
                          current_coords[1])
        coords[current] = current_coords
    max_coords['right'] = current_coords
    while current_coords[1] <= max_coords['up'][1]:
        current += 1
        current_coords = (current_coords[0],
                          current_coords[1] + 1)
        coords[current] = current_coords
    max_coords['up'] = current_coords
    while current_coords[0] >= max_coords['left'][0]:
        current += 1
        current_coords = (current_coords[0] - 1,
                          current_coords[1])
        coords[current] = current_coords
    max_coords['left'] = current_coords
    while current_coords[1] >= max_coords['down'][0]:
        current += 1
        current_coords = (current_coords[0],
                          current_coords[1] - 1)
        coords[current] = current_coords
    max_coords['down'] = current_coords

#Part 1 answer
num = 368078
x,y = coords[num]
print abs(x)+abs(y)

#mathematical
#num = 2 #368078
# when we make square we add first 1 then 2,3 then 4,5
# i.e. 4 times 2 numbers. Then for second layer 4 times a tuple of
# 4 numbers: 10,11,12,13; then 14,15,16,17,18 etc
# hence we are adding 1 then 8 then 16 i.e. in multiples of 8
# for a number x in layer n the value (x-2)%(2n) lies b/w 0 and n-1
# hence we transform
# 17 16 15 14 13
# 18 5  4  3  12
# 19 6  1  2  11
# 20 7  8  9  10
# 21 22 23 24 25
# into
# 3 2 1 0 3
# 0 1 0 1 2
# 1 0 1 0 1
# 2 1 0 1 0
# 3 0 1 2 3
new_num = num -1
i =  int(math.sqrt(new_num / 4.0))
'''
while new_num >= 8*i:
       new_num = new_num - 8*i
       i += 1
'''
pre_answer = (num - 2) % (2 * i)
if pre_answer < i - 1:
    answer = i*2 - 1 - pre_answer
else:
    answer = pre_answer + 1
print answer

# Part 2 definition


def getSum((x, y)):
    sum_adj = 0
    max_neighbours = 9
    for coord in coords:
        diff_x = abs(coord[0]-x)
        diff_y = abs(coord[1]-y)
        if diff_x <= 1 and diff_y <= 1:
            sum_adj += coords[coord]
            max_neighbours -= 1
            if max_neighbours <= 0:
                break
    return sum_adj

coords = {(0,0):1}
max_coords = {'left':(0,0),
           'right':(0,0),
           'up':(0,0),
           'down':(0,0)}

end = 325489#368080
last_sum = 1
current_coords = (0,0)
while last_sum <= end:
    #go left
    while current_coords[0] <= max_coords['right'][0]:
        current_coords = (current_coords[0] + 1,
                          current_coords[1])
        last_sum = getSum(current_coords)
        coords[current_coords] = last_sum
        if last_sum > end:
            break
    max_coords['right'] = current_coords
    if last_sum > end:
        break
    while current_coords[1] <= max_coords['up'][1]:
        current_coords = (current_coords[0],
                          current_coords[1] + 1)
        last_sum = getSum(current_coords)
        coords[current_coords] = last_sum
        if last_sum > end:
            break
    max_coords['up'] = current_coords
    if last_sum > end:
        break
    while current_coords[0] >= max_coords['left'][0]:
        current_coords = (current_coords[0] - 1,
                          current_coords[1])
        last_sum = getSum(current_coords)
        coords[current_coords] = last_sum
        if last_sum > end:
            break
    max_coords['left'] = current_coords
    if last_sum > end:
        break
    while current_coords[1] >= max_coords['down'][0]:
        current_coords = (current_coords[0],
                          current_coords[1] - 1)
        last_sum = getSum(current_coords)
        coords[current_coords] = last_sum
        if last_sum > end:
            break
    max_coords['down'] = current_coords
    if last_sum > end:
        break
print last_sum
