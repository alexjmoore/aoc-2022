import string

from collections import defaultdict

with open('input.txt') as input:
    # pull in the current crate layout
    raw = ''
    for line in input:
        if line.isspace():
            break
        raw += line
    data = raw.split('\n')[:-1]
    stackcount = int(data.pop().split()[-1])
    
    # create dict structure of crate layout
    crates = defaultdict(list)
    for stack in data:
        for x in range(1,stackcount+1):
            crate = stack[(x*4)-3]
            if not crate.isspace():
                crates[x].insert(0, crate)

    # pull in the moves and move crates
    for line in input:
        line = line.split()
        count, source, dest = int(line[1]), int(line[3]), int(line[5])
        crates[dest] = crates[dest] + crates[source][-count:]
        crates[source] = crates[source][:-count]

    # figure out the top crates
    topcrates = ''
    for stack in sorted(crates):
        topcrates += crates[stack][-1]
    
    print(f"top crates for CrateMove 9001 are: {topcrates}")





