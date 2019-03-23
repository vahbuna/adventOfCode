from itertools import islice, cycle

def part_one(steps=3, iterations=2018, after=2017):
    pos = 0
    #state = []
    for i in range(iterations):
        #state.insert(pos, i)
        pos = (pos + steps) % (i + 1) + 1
        if pos == 1:
            print i+1
        '''
        slicer = islice(cycle(state), pos, None, steps)
        elem = slicer.next()
        elem = slicer.next()
        pos = state.index(elem)
        pos += 1
        '''
        #pos = 1 + islice(circ_state, pos, None, steps).next()
    #idx = state.index(after)
    #print state[idx+1]
if __name__ == "__main__":
    part_one(303, 30000000, 0)
