from collections import defaultdict
import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def load_data():
    ins = []
    with open('Day18.input', 'r') as in_file:
        for line in in_file:
            ins.append(line.strip())
    return ins

queue = defaultdict(list)
send_count = defaultdict(int)

def part_two():
    p0 = threading.Thread(target=worker, args=(0,))
    p0.start()
    p1 = threading.Thread(target=worker, args=(1,))
    p1.start()


def worker(pid):
    global queue
    global send_count
    registers = defaultdict(int)
    registers['p'] = pid
    inst = load_data()
    last = len(inst)
    i = 0
    while i < last:
        fields = inst[i].split()
        #print 'In '+ str(pid) + 'parsing '+str(i)
        if len(fields) == 3:
            try:
                val = int(fields[2])
            except ValueError:
                val = registers[fields[2]]
            try:
                var = int(fields[1])
            except ValueError:
                var = registers[fields[1]]
            if fields[0] == 'set':
                registers[fields[1]]=val
            elif fields[0] == 'add':
                registers[fields[1]] += val
            elif fields[0] == 'mul':
                registers[fields[1]] *= val
            elif fields[0] == 'mod':
                registers[fields[1]] %= val
            elif fields[0] == 'jgz':
                if var > 0:
                    i += val
                    continue
        else:
            try:
                val = int(fields[1])
            except ValueError:
                val = registers[fields[1]]
            if fields[0] == 'snd':
                logging.debug("{0} sending {1}".format(pid,val))
                queue[(1+pid)%2].append(val)
                send_count[pid] += 1
                logging.debug("{0} count {1}".format(pid, send_count[pid]))
            elif fields[0] == 'rcv':
                if len(queue[pid]) > 0:
                    registers[fields[1]] = queue[pid].pop(0)
                else:
                    time.sleep(10)
                    registers[fields[1]] = queue[pid].pop(0)
        i += 1

def part_one():
    inst = load_data()
    last = len(inst)
    registers = defaultdict(int)
    i = 0
    played = []
    while True:
        fields = inst[i].split()
        if len(fields) == 3:
            try:
                val = int(fields[2])
            except ValueError:
                val = registers[fields[2]]
            if fields[0] == 'set':
                registers[fields[1]]=val
            elif fields[0] == 'add':
                registers[fields[1]] += val
            elif fields[0] == 'mul':
                registers[fields[1]] *= val
            elif fields[0] == 'mod':
                registers[fields[1]] %= val
            elif fields[0] == 'jgz':
                if registers[fields[1]] > 0:
                    i += val
                    continue
        else:
            if fields[0] == 'snd':
                played.append(registers[fields[1]])
            elif fields[0] == 'rcv':
                if registers[fields[1]] > 0:
                    print played[-1]
                    break
        i += 1

if __name__ == "__main__":
    global queue
    global send_count
    try:
        part_two()
    except IndexError:
        print send_count
