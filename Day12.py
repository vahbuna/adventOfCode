from collections import defaultdict


def get_data():
    info = defaultdict(list)
    with open('Day12.input' ,'r') as ifile:
        for line in ifile:
            x,y = line.strip().split('<->')
            info[int(x.strip())].extend([int(i.strip()) for i in y.split(',')])
    return info

def part_one():
    node_list = get_data()
    visited = []
    to_visit = [0]
    while to_visit:
        node = to_visit.pop(0)
        visited.append(node)
        for neighbour in node_list[node]:
            if neighbour not in visited and neighbour not in to_visit:
                to_visit.append(neighbour)
    print len(visited)


def part_two():
    node_list = get_data()
    visited = []
    to_visit = []
    groups = 0
    for origin in node_list.keys():
        if origin in visited:
            continue
        groups += 1
        to_visit.append(origin)
        while to_visit:
            node = to_visit.pop(0)
            visited.append(node)
            for neighbour in node_list[node]:
                if neighbour not in visited and neighbour not in to_visit:
                    to_visit.append(neighbour)
    print groups

if __name__ == "__main__":
    part_two()

