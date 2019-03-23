from collections import defaultdict

def get_data():
    data = defaultdict(list)
    with open('Day13.input', 'r') as in_file:
        for line in in_file:
            d, r = line.strip().split(':')
            data[int(d)] = [0]*int(r)
    return data

def part_one():
    firewall = get_data()
    pos = {}
    dir_sc = {}
    max_depth = max(firewall.keys())
    #init
    for depth, layer in firewall.iteritems():
        pos[depth] = 0
        dir_sc[depth] = 1
    sev = 0
    for ps in range(max_depth+1):
        if ps in firewall and pos[ps] == 0:
            sev += ps * len(firewall[ps])
        for depth, layer in firewall.iteritems():
            pos[depth] += dir_sc[depth]
            if pos[depth] < 0:
                    pos[depth] = min(1, len(layer)-1)
                    dir_sc[depth] = 1
            elif pos[depth] >= len(layer):
                pos[depth] = len(layer) - 2
                dir_sc[depth] = -1
    print sev

def part_two():
    firewall = get_data()
    div = {}
    for depth, layer in firewall.iteritems():
        div[depth] = (len(layer) - 1) * 2
    t = 0
    while True:
        for depth in firewall:
            if (t+depth)%div[depth] == 0:
                break
        else:
            print t, 'Yeah'
            break
        t += 1


if __name__ == "__main__":
   part_two()

