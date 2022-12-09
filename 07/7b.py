fs = {}

def totalDir(dir): 
    subdir_size = 0
    for subdir in fs[dir]['subdirs']:
        totalDir(subdir)
        subdir_size += fs[subdir]['total_size']
    fs[dir]['total_size'] = fs[dir]['this_size'] + subdir_size

with open('input.txt') as input:
    output = []
    while line := input.readline().strip():
        if line.startswith('$'):
            output.append([line,[]])
        else:
            output[-1][1].append(line)

    cwd = []
 
    for command in output:
        if command[0][2:4] == 'cd':
            
            if command[0][5:] == '..':
                cwd.pop()
            else:
                cwd.append(command[0][5:])
        elif command[0][2:4] == 'ls':
                for data in command[1]:
                    if data.startswith('dir'):
                        subdir = '/'.join(cwd) + '/' + data[4:]
                        try:
                            fs['/'.join(cwd)]['subdirs'].append(subdir)
                        except KeyError:
                            fs['/'.join(cwd)] = { 'total_size': 0, 'this_size': 0, 'subdirs': []}
                            fs['/'.join(cwd)]['subdirs'].append(subdir)
                    else:
                        size = int(data.split()[0])
                        try:
                            fs['/'.join(cwd)]['this_size'] += size
                        except KeyError:
                            fs['/'.join(cwd)] = { 'total_size': 0, 'this_size': size, 'subdirs': []}  
   
    totalDir(list(fs.keys())[0])
    
    sum_of_10k = 0
    for dir in fs.keys():
        if fs[dir]['total_size'] <= 100000:
            sum_of_10k += fs[dir]['total_size']
    print(f"sum of directories up to 10k: {sum_of_10k}")

    root_size = fs['/']['total_size']
    total_size = 70000000

    curr_free_space = total_size - root_size

    delta_needed = 30000000 - curr_free_space

    print(f"root: {root_size} free: {curr_free_space} delta: {delta_needed}")
    
    sorted_dirs = sorted(fs, key=lambda x: (fs[x]['total_size']), reverse=True)
    sorted_dirs.pop(0) # remove /
    prev = ''
    for x in sorted_dirs:
        if fs[x]['total_size'] >= delta_needed:
            prev = x
        else:
            break
    
    print(f"found best candidate: {prev} size: {fs[prev]['total_size']}")