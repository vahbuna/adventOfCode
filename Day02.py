import csv
import numpy as np

list_array =[]
sum = 0

def getDivisibles(row):
    for i, num in enumerate(row):
        for b in row[i+1:]:
            if num<b and b%num == 0:
                return b/num
            elif num>b and num%b == 0:
                return num/b

with open('Day02.input', 'r') as input_file:
    data = csv.reader(input_file, delimiter='\t')
    for row in data:
        temp_list = [int(x) for x in row]
        sum += getDivisibles(temp_list)
        list_array.append(temp_list)

chksum_matrix = np.array(list_array)
print np.sum(np.amax(chksum_matrix, axis=1) - \
    np.amin(chksum_matrix, axis=1))

print sum
