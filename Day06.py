import numpy as np
import copy
from itertools import cycle

history = []
current_memory = []
with open('Day06.input', 'r') as input_file:
    for line in input_file:
        current_memory = [int(x) for x in line.strip().split()]

num_banks = len(current_memory)
while current_memory not in history:
    history.append(copy.copy(current_memory))
    max_pos = np.argmax(current_memory)
    max_val = current_memory[max_pos]
    index_cycle = cycle(range(max_pos+1,num_banks)+range(max_pos+1))
    current_memory[max_pos] = 0
    update = max_val / num_banks
    remain = max_val % num_banks
    if update > 0:
        for i in range(num_banks):
            current_memory[index_cycle.next()] += update
    for i in range(remain):
        current_memory[index_cycle.next()] += 1
# part 1
print len(history)

#part 2
print len(history) - history.index(current_memory)
