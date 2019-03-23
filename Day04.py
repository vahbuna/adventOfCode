from collections import Counter

# Part 1
num_valid = 0
with open('Day04.input', 'r') as input_file:
    for line in input_file:
        passphrases = Counter(line.strip().split())
        elem, count = passphrases.most_common(1)[0]
        if count == 1:
            num_valid += 1

print num_valid

# Part 2
num_valid = 0
with open('Day04.input', 'r') as input_file:
    for line in input_file:
        passphrases = line.strip().split()
        counts = ["".join(sorted(phrase)) for phrase in passphrases]
        if len(counts) == len(set(counts)):
            num_valid += 1

print num_valid
